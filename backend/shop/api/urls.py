from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, ProductCategoryViewSet, ShopViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename='product')
router.register(r"products-categories", ProductCategoryViewSet, basename='product-category')
router.register(r"shops", ShopViewSet, basename='shop')

urlpatterns = [
    path("shop/", include(router.urls)),
]
