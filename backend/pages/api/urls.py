from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (LayoutViewSet, PageViewSet, DocumentViewSet,
                    CookiesSnackbarViewSet, CookiesPreferencesViewSet)

router = DefaultRouter()
router.register(r"layouts", LayoutViewSet, basename='layout')
router.register(r"pages", PageViewSet, basename='page')
router.register(r"documents", DocumentViewSet, basename='document')
router.register(r"cookies_snackbar", CookiesSnackbarViewSet, basename='cookies_snackbar')
router.register(r"cookies_preferences", CookiesPreferencesViewSet, basename='cookies_preferences')

urlpatterns = [
    path("", include(router.urls)),
]
