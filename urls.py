# """
# URL configuration for task_management project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
]




from django.urls import path
from .views import project_list, project_create, project_update, project_delete, task_list, task_create, task_update, task_delete

urlpatterns = [
    # Project URLs
    path('projects/', project_list, name='project_list'),
    path('projects/create/', project_create, name='project_create'),
    path('projects/update/<int:pk>/', project_update, name='project_update'),
    path('projects/delete/<int:pk>/', project_delete, name='project_delete'),

    # Task URLs
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/update/<int:pk>/', task_update, name='task_update'),
    path('tasks/delete/<int:pk>/', task_delete, name='task_delete'),
]

