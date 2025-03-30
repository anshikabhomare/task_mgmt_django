from django.apps import AppConfig


# class TasksConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'tasks'
class TaskManagementConfig(AppConfig):  # Rename the class properly
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_management'  # Use the correct app name
