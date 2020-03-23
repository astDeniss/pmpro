
from django.urls import path
from .views import ProjectListView, add_project

urlpatterns = [

    path('projects/', ProjectListView.as_view(), name="projects-list"),
    path('projects/add/', add_project, name="add-project"),

]