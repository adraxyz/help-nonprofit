from modeltranslation.translator import register, TranslationOptions
from .models import Project, ProjectCategory


@register(ProjectCategory)
class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "description")


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("title", "slug", "subtitle", "description",
              "country", "region", "city", "address")
