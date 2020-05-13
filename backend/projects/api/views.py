from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProjectSerializer, FullProjectSerializer, ProjectCategorySerializer
from ..models import Project, ProjectCategory


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_serializer_class(self):
        full_data = self.request.query_params.get('full_data', None)
        if full_data:
            return FullProjectSerializer
        return self.serializer_class


class ProjectCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectCategorySerializer
    queryset = ProjectCategory.objects.all()
    lookup_field = 'title'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
