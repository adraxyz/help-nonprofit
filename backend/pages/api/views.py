from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (LayoutSerializer, PageSerializer, DocumentSerializer,
                          CookiesSnackbarSerializer, CookiesPreferencesSerializer)
from ..models import Layout, Page, Document, CookiesSnackbar, CookiesPreferences


class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    lookup_field = 'name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class LayoutViewSet(viewsets.ModelViewSet):
    serializer_class = LayoutSerializer
    queryset = Layout.objects.all()
    lookup_field = 'name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    lookup_field = 'type'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class CookiesSnackbarViewSet(viewsets.ModelViewSet):
    serializer_class = CookiesSnackbarSerializer
    queryset = CookiesSnackbar.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class CookiesPreferencesViewSet(viewsets.ModelViewSet):
    serializer_class = CookiesPreferencesSerializer
    queryset = CookiesPreferences.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
