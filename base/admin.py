from django.contrib import admin
from .models import Project, Tag

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name',)  # Adds a search box to the admin to search by 'name'
    list_display = ('name', 'description', 'link')  # Fields to display in the admin list view
    list_filter = ('name',)  # Optional: Filter options in the admin sidebar
    filter_horizontal = ('tags',)  # Adds a horizontal filter widget for the tags field


# Register the model with the admin site
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)

