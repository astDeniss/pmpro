from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import ProjectListView, add_project, ProjectDetailView, ProjectDeleteView, TaskListView

urlpatterns = [

    path('projects/', login_required(ProjectListView.as_view()), name="projects-list"),
    path('projects/add/', login_required(add_project), name="add-project"),
    path('projects/<int:pk>/', login_required(ProjectDetailView.as_view()), name="project-detail"),
    path('projects/delete/<int:pk>/', login_required(ProjectDeleteView.as_view()), name="project-delete"),
    path('tasks/', login_required(TaskListView.as_view()), name="tasks-list"),

]