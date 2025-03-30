from django.contrib import admin
from .models import Project, Task, UserProfile

# ProjectAdmin to customize how Project is displayed in Django Admin
class ProjectAdmin(admin.ModelAdmin):
    # Fields to be displayed in the project list
    list_display = ('name', 'start_date', 'end_date', 'status')  # Include these fields in the list view
    list_filter = ('status',)  # Filter by status
    search_fields = ('name',)  # Search by project name

# TaskAdmin to customize how Task is displayed in Django Admin
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assigned_to', 'status', 'due_date')  # Display relevant task fields
    list_filter = ('status', 'project')  # Filter tasks by status and project
    search_fields = ('title', 'assigned_to__username')  # Search tasks by title or assigned user

# UserProfileAdmin to display user role information in Django Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Display username and role
    search_fields = ('user__username',)  # Search by username

# Register models with their respective Admin configurations
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile, UserProfileAdmin)