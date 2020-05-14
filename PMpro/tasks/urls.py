from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import ProjectListView, add_project, add_task, \
    ProjectDetailView, ProjectDeleteView, TaskUpdateView, TaskDeleteView, \
    TaskListView, ProjectUpdateView, project_analytics

urlpatterns = [

    path('projects/', login_required(ProjectListView.as_view()), name="projects-list"),
    path('projects/add/', login_required(add_project), name="add-project"),
    path('projects/<int:pk>/', login_required(ProjectDetailView.as_view()), name="project-detail"),
    path('projects/delete/<int:pk>/', login_required(ProjectDeleteView.as_view()), name="project-delete"),
    path('projects/update/<int:pk>/', login_required(ProjectUpdateView.as_view()), name="project-update"),
    path('task/update/<int:pk>/', login_required(TaskUpdateView.as_view()), name="task-update"),
    path('task/delete/<int:pk>/', login_required(TaskDeleteView.as_view()), name="task-delete"),
    path('tasks/', login_required(TaskListView.as_view()), name="tasks-list"),
    path('projects/analytics/<int:pk>/', login_required(project_analytics), name="project-analytics"),
    path('tasks/add/', login_required(add_task), name="add-task"),

]