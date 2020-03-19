from django.contrib import admin
from .models import Manager, Project, Task

admin.site.register(Project)
admin.site.register(Task)
