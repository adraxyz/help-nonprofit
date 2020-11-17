from django.contrib import admin
from .models import Product, ProductCategory, Shipment, Shop


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",),
        "slug_it": ("title_it",),
        "slug_en": ("title_en",)
    }


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Shipment)
admin.site.register(Shop)
