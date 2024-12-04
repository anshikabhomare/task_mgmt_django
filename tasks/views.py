

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task,Project,User
from django.contrib.auth.decorators import login_required

# --- CRUD for Project ---

# List all projects
@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/project_list.html', {'projects': projects})

# Create a new project
@login_required
def project_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        project = Project.objects.create(name=name, description=description)
        project.users.set(request.POST.getlist('users'))  # Assign users
        return redirect('project_list')

    users = User.objects.all()
    return render(request, 'tasks/project_form.html', {'users': users})

# Update an existing project
@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.name = request.POST['name']
        project.description = request.POST['description']
        project.users.set(request.POST.getlist('users'))  # Update users
        project.save()
        return redirect('project_list')

    users = User.objects.all()
    return render(request, 'tasks/project_form.html', {'project': project, 'users': users})

# Delete a project
@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'tasks/project_confirm_delete.html', {'project': project})

# --- CRUD for Task ---

# List all tasks
@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Create a new task
@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        assigned_to_id = request.POST['assigned_to']
        project_id = request.POST['project']

        assigned_to = get_object_or_404(User, id=assigned_to_id)
        project = get_object_or_404(Project, id=project_id)

        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            assigned_to=assigned_to,
            project=project,
        )
        return redirect('task_list')

    users = User.objects.all()
    projects = Project.objects.all()
    return render(request, 'tasks/task_form.html', {'users': users, 'projects': projects})

# Update an existing task
@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        assigned_to_id = request.POST['assigned_to']
        project_id = request.POST['project']

        task.assigned_to = get_object_or_404(User, id=assigned_to_id)
        task.project = get_object_or_404(Project, id=project_id)

        task.save()
        return redirect('task_list')

    users = User.objects.all()
    projects = Project.objects.all()
    return render(request, 'tasks/task_form.html', {'task': task, 'users': users, 'projects': projects})

# Delete a task
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})










from rest_framework import viewsets
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

# ViewSet for Project
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# ViewSet for Task
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
