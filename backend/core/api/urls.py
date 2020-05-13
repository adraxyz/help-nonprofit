from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscribeView, ContactFormView, LabelViewSet

router = DefaultRouter()
router.register(r"labels", LabelViewSet, basename='label')


urlpatterns = [
    path("subscribe", SubscribeView.as_view()),
    path("contact_form", ContactFormView.as_view()),
    path("", include(router.urls)),
]
