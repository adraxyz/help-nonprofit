from modeltranslation.translator import register, TranslationOptions
from .models import Product, ProductCategory


@register(ProductCategory)
class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "description")


@register(Product)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("title", "slug", "subtitle", "description")
