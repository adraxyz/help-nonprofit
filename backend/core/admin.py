from django.contrib import admin
from .models import Message, Label, CookiesCategory, CookiesProvider, Cookie


class LabelModelAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'topic', 'item', 'label')
    list_filter = ('topic', 'item', 'label')


class MessageModelAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'text', 'topic', 'text_to_users')
    list_filter = ('text', 'topic', 'text_to_users')


class CookiesCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title')
    list_filter = ('name', 'title')


class CookiesProviderModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'category')
    list_filter = ('name', 'title')


class CookieModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'provider', 'duration')
    list_filter = ('name', 'title')


admin.site.register(Label, LabelModelAdmin)
admin.site.register(Message, MessageModelAdmin)
admin.site.register(CookiesCategory, CookiesCategoryModelAdmin)
admin.site.register(CookiesProvider, CookiesProviderModelAdmin)
admin.site.register(Cookie, CookieModelAdmin)
