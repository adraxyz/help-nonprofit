from django.contrib import admin
from .models import Project, ProjectCategory


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",),
        "slug_it": ("title_it",),
        "slug_en": ("title_en",)
    }


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory)
