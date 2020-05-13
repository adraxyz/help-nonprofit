from rest_framework import serializers
from ..models import Message, Label


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['text', 'topic', 'text_to_users']


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = ['topic', 'item', 'label']
