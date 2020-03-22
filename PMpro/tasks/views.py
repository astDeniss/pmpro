from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Project
from users.models import Manager


class ProjectListView(ListView):
    model = Project
    template_name = "projects.html"
    paginate_by = 20

    # returns a query_set of projects, where currently logged_in user is set as Manager for the project
    def get_queryset(self):
        current_user = self.request.user
        manager_with_current_user = Manager.objects.get(user=current_user)
        return Project.objects.filter(manager=manager_with_current_user).order_by("created_at")
