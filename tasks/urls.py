from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views  # Importing views from the tasks app

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)  # Registering the Project viewset
router.register(r'tasks', views.TaskViewSet)  # Registering the Task viewset

# URL patterns for the app
urlpatterns = [
    # You can add more custom views if necessary
    # For example, if you have other views to display lists or create tasks
]

# Adding the router's URLs to the urlpatterns
urlpatterns += router.urls  # This automatically includes '/api/projects/' and '/api/tasks/' endpoints
