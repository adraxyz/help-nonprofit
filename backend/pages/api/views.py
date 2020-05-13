from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LayoutSerializer, PageSerializer
from ..models import Layout, Page


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
