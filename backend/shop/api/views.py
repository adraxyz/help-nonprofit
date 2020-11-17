from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer, ProductCategorySerializer, ShopSerializer
from ..models import Product, ProductCategory, Shop


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(active=True)
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class ProductCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.filter(active=True)
    lookup_field = 'title'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
