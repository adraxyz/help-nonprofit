from modeltranslation.translator import register, TranslationOptions
from .models import Product, ProductCategory


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "description")


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "slug", "subtitle", "description")
