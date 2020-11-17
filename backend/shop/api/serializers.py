from rest_framework import serializers
from ..models import Product, ProductCategory, Shop


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ["order", "title", "subtitle", "description", "icon",
                  "internal", "active"]


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["order", "title", "subtitle", "description",
                  "slug", "slug_it", "slug_en", "image_0", "image_1", "image_2",
                  "thumbnail", "video", "price", "active", "category",
                  "availability", "shop_link"]


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ["slug", "payment_link", "shipping_fees"]
