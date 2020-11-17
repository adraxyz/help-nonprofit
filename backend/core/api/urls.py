from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SubscribeView, ContactFormView, LabelViewSet,
                    CookiesCategoryViewSet, ShipmentFormView)

router = DefaultRouter()
router.register(r"labels", LabelViewSet, basename='label')
router.register(r"cookies_categories", CookiesCategoryViewSet, basename='cookies_categories')


urlpatterns = [
    path("subscribe", SubscribeView.as_view()),
    path("contact_form", ContactFormView.as_view()),
    path("shipment_form", ShipmentFormView.as_view()),
    path("", include(router.urls)),
]
