from django.contrib import admin
from .models import Message, Label


class LabelModelAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'topic', 'item', 'label')
    list_filter = ('topic', 'item', 'label')


class MessageModelAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'text', 'topic', 'text_to_users')
    list_filter = ('text', 'topic', 'text_to_users')


admin.site.register(Label, LabelModelAdmin)
admin.site.register(Message, MessageModelAdmin)
