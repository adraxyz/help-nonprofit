from rest_framework import serializers
from ..models import Project, ProjectCategory
from pages.api.serializers import (
    TextSerializer, ImageSerializer,VideoSerializer, ButtonSerializer, DocumentSerializer
)


class ProjectCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectCategory
        fields = ["order", "title", "subtitle", "description", "image"]


class ProjectSerializer(serializers.ModelSerializer):
    buttons = ButtonSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["order", "title", "subtitle", "slug", "thumbnail", "buttons"]


class FullProjectSerializer(ProjectSerializer):
    texts = TextSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)
    category = ProjectCategorySerializer(read_only=True)

    class Meta:
        model = Project
        fields = ["order", "title", "slug", "subtitle", "description", "thumbnail", "budget",
                  "category", "country", "region", "city", "address", "latitude", "longitude",
                  "texts", "images", "videos", "buttons", "documents"]
