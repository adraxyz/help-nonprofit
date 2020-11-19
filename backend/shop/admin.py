from django.contrib import admin
from .models import Product, ProductCategory, Shipment, Shop


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",),
        "slug_it": ("title_it",),
        "slug_en": ("title_en",)
    }


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'timestamp', 'state')
    list_filter = ('email', 'timestamp', 'state')


admin.site.register(Product, ProductAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(ProductCategory)
admin.site.register(Shop)
