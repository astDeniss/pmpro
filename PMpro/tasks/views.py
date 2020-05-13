from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Project, Task
from users.models import Manager
from .forms import ProjectForm, TaskForm
from datetime import datetime, timezone


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


def add_task(request):
    project_titles = Project.objects.all()
    
    if request.method == "POST": 
        form = TaskForm(request.POST) 
        if form.is_valid():
            form.save()
            
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            deadline = form.cleaned_data.get('deadline')
            project = form.cleaned_data.get('project')

            task = Task(title=title, description=description, deadline=deadline, project_id="project")
            #task.save()
            return redirect('tasks-list')
    else:
        form = TaskForm()
        args = {'form': form, "project_titles":project_titles}
        return render(request, 'create_new_task.html', args)


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('projects-list')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project_update.html'
    fields = ['title', 'deadline', 'description', 'status']
    success_url = reverse_lazy('projects-list')


class TaskListView(ListView):
    model = Project
    template_name = "tasks.html"
    paginate_by = 7

    # returns a query_set of projects, where currently logged_in user is set as Manager for the project
    def get_queryset(self):
        current_user = self.request.user
        manager_with_current_user = Manager.objects.get(user=current_user)
        return Project.objects.filter(manager=manager_with_current_user).order_by("deadline")


def project_analytics(request, pk):
    try:
        project = Project.objects.get(pk=pk)
        total_tasks = 0
        completed_tasks = 0

        for task in project.tasks.all():
            if task.status == "Completed":
                completed_tasks += 1
            total_tasks += 1

        tasks_left = total_tasks - completed_tasks
        spent_on_project = datetime.now(timezone.utc) - project.created_at
        days_spent = spent_on_project.days
        procent_completed = (completed_tasks/total_tasks)*100

    except Project.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'project_analytics.html',
                  {'project': project,
                   'total_tasks': total_tasks,
                   'completed_tasks': completed_tasks,
                   'tasks_left': tasks_left,
                   'days_spent': days_spent,
                   'procent_completed': procent_completed,
                   }
                  )
