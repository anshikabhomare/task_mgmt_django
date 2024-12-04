from django.db import models
from django.contrib.auth.models import User

# UserProfile model for user roles
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)  # e.g., 'Manager', 'Team Member'

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Project model
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='projects')  # Many-to-many relationship

    def __str__(self):
        return self.name

# Task model
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # Link to the Project
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User (who the task is assigned to)
    status = models.CharField(max_length=100)  # Status of the task (e.g., 'Not Started', 'In Progress')
    due_date = models.DateTimeField()  # Task due date

    def __str__(self):
        return self.title
