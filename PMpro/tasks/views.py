from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Project
from users.models import Manager
from .forms import ProjectForm
import datetime


class ProjectListView(ListView):
    model = Project
    template_name = "projects.html"
    paginate_by = 20

    # returns a query_set of projects, where currently logged_in user is set as Manager for the project
    def get_queryset(self):
        current_user = self.request.user
        manager_with_current_user = Manager.objects.get(user=current_user)
        return Project.objects.filter(manager=manager_with_current_user).order_by("deadline")


def add_project(request):
    if request.method == "POST":
        current_user = request.user
        current_manager = Manager.objects.get(user=current_user)

        form = ProjectForm(request.POST, instance=current_manager)  # since manager is a required field- we are
        # pre-loding it into the form
        if form.is_valid():
            form.save()

            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            deadline = form.cleaned_data.get('deadline')

            our_project = Project(manager=current_manager, title=title, description=description, deadline=deadline)
            our_project.save()
            return redirect('projects-list')
    else:
        form = ProjectForm()
        return render(request, 'create_new_project.html', {'form': form})


class ProjectDetailView(DetailView):

    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'
