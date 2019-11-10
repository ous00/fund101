from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Project
# Register your models here.

class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project 

class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource

admin.site.register(Project, ProjectAdmin)


