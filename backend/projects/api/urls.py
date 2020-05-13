from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProjectViewSet, ProjectCategoryViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename='project')
router.register(r"projects-categories", ProjectCategoryViewSet, basename='project-category')

urlpatterns = [
    path("", include(router.urls)),
]
