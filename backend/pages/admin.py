from django.contrib import admin
from .models import (Layout, Footer, Socials, Page, Section, Text,
                     Image, Video, Button, Document)
from django.conf import settings
from django.forms import fields
from .utils import RoutingUtils
import os

ru = RoutingUtils(os.path.join(settings.FRONTEND_DIR, "pages"))


class PageAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'order', 'name', 'title')
    list_filter = ('order', 'name', 'title')

    def get_form(self, request, obj=None, change=False, **kwargs):
        """
        We have to override the form because of the newly created projects.
        We must consider them for the page 'name'.
        """
        name_choices = [
            (r[1:] if r != "/" else "home", r[1:] if r != "/" else "home")
            for r in ru.get_nuxt_routes()
        ]
        form = super().get_form(request, obj, change, **kwargs)
        for k, v in form.base_fields.items():
            if k.startswith("name"):
                v.choices = name_choices
        return form


class SectionModelAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'page', 'order', 'title')
    list_filter = ('page', 'order', 'title')


class PageFeatureModelAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'section', 'order', 'project', 'project_section')
    list_filter = ('section', 'order', 'project', 'project_section')


class ButtonAdmin(PageFeatureModelAdmin):

    def get_form(self, request, obj=None, change=False, **kwargs):
        """
        We have to override the form because of the newly created projects.
        We must consider them for the property 'to' of the button.
        """
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields["to"].choices = [(r, r) for r in ru.get_nuxt_routes()]
        return form


admin.site.register(Layout)
admin.site.register(Footer)
admin.site.register(Socials)
admin.site.register(Page, PageAdmin)
admin.site.register(Section, SectionModelAdmin)
admin.site.register(Text, PageFeatureModelAdmin)
admin.site.register(Image, PageFeatureModelAdmin)
admin.site.register(Video, PageFeatureModelAdmin)
admin.site.register(Button, ButtonAdmin)
admin.site.register(Document, PageFeatureModelAdmin)
