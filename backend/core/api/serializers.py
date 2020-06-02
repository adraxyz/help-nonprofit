from rest_framework import serializers
from ..models import Message, Label, CookiesCategory, CookiesProvider, Cookie


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['text', 'topic', 'text_to_users']


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = ['topic', 'item', 'label']


class CookieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cookie
        fields = ['name', 'title', 'purpose', 'provider', 'duration']


class CookiesProviderSerializer(serializers.ModelSerializer):
    cookies = CookieSerializer(many=True, read_only=True)

    class Meta:
        model = CookiesProvider
        fields = ['name', 'title', 'description', 'default', 'readonly', 'category', 'cookies']


class CookiesCategorySerializer(serializers.ModelSerializer):
    cookies_providers = CookiesProviderSerializer(many=True, read_only=True)

    class Meta:
        model = CookiesCategory
        fields = ['name', 'title', 'description', 'cookies_providers']



