from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LayoutViewSet, PageViewSet

router = DefaultRouter()
router.register(r"layouts", LayoutViewSet, basename='layout')
router.register(r"pages", PageViewSet, basename='page')

urlpatterns = [
    path("", include(router.urls)),
]
