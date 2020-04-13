
from django.urls import path
from .views import ProjectListView, add_project, ProjectDetailView, ProjectDeleteView

urlpatterns = [

    path('projects/', ProjectListView.as_view(), name="projects-list"),
    path('projects/add/', add_project, name="add-project"),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name="project-detail"),
    path('projects/delete/<int:pk>/', ProjectDeleteView.as_view(), name="project-delete"),

]