from django.db import models
from users.models import Manager

status_choices = [
    ('Unassigned', 'Unassigned'),
    ('In progress', 'In progress'),
    ('Completed', 'Completed'),
]


class Project(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=status_choices, default="Unassigned")

    def __str__(self):
        return "{} - {}".format(self.title, self.description)


class Task(models.Model):
    priority_choices = [
        ('Low', 'Low'),
        ('Middle', 'Middle'),
        ('High', 'High'),
        ('URGENT', 'URGENT'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=status_choices, default="Unassigned")
    priority = models.CharField(max_length=50, choices=priority_choices, default="Low")

    def __str__(self):
        return "{} {}".format(self.title, self.description)
