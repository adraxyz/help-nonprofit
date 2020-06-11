from rest_framework import serializers
from ..models import (Layout, Page, Section, Text, Image, Video, Button, Footer,
                      Social, Document, MetaTag, CookiesSnackbar, CookiesPreferences)


class MetaTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetaTag
        fields = ['hid', 'name', 'content']


class TextSerializer(serializers.ModelSerializer):
    meta_tags = MetaTagSerializer(many=True, read_only=True)

    class Meta:
        model = Text
        fields = ['order', 'title', 'subtitle', 'content', 'project_section', 'meta_tags']


class ImageSerializer(serializers.ModelSerializer):
    meta_tags = MetaTagSerializer(many=True, read_only=True)

    class Meta:
        model = Image
        fields = ['order', 'content', 'alt_content', 'alt', 'project_section', 'meta_tags']


class VideoSerializer(serializers.ModelSerializer):
    meta_tags = MetaTagSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ['order', 'content', 'poster', 'meta_tags']


class ButtonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Button
        fields = ['order', 'to', 'text_0', 'text_1', 'href', 'target', 'project_section']


class DocumentSerializer(serializers.ModelSerializer):
    meta_tags = MetaTagSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ['order', 'title', 'subtitle', 'description',
                  'file', 'project_section', 'meta_tags', 'type']


class SectionSerializer(serializers.ModelSerializer):
    texts = TextSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    buttons = ButtonSerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)
    meta_tags = MetaTagSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['texts', 'images', 'videos', 'buttons', 'documents',
                  'order', 'title', 'subtitle', 'meta_tags']


class PageSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    meta_tags = MetaTagSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['order', 'name', 'title', 'navigation', 'sections', 'meta_tags']
        lookup_field = 'name'


class FooterSerializer(serializers.ModelSerializer):
    document_0 = DocumentSerializer(read_only=True)
    document_1 = DocumentSerializer(read_only=True)

    class Meta:
        model = Footer
        fields = ['corporate_full_name', 'corporate_short_name', 'footer_1_col_title',
                  'footer_2_col_title', 'footer_3_col_title', 'transparency_title',
                  'document_0', 'document_1', 'registered_office', 'subscribe_btn_text',
                  'footer_1_col_text', 'footer_2_col_text', 'footer_3_col_text', 'email',
                  'fiscal_code', 'registered_office', 'donation_title']


class SocialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Social
        fields = ['order', 'platform', 'link']


class LayoutSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)
    logo = ImageSerializer(read_only=True)
    donation_button = ButtonSerializer(read_only=True)
    contact_button = ButtonSerializer(read_only=True)
    footer = FooterSerializer(read_only=True)
    meta_tags = MetaTagSerializer(many=True, read_only=True)

    class Meta:
        model = Layout
        fields = ['name', 'pages', 'logo', 'donation_button', 'meta_tags',
                  'contact_button', 'footer']
        lookup_field = 'name'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if 'pages' in ret:
            pages = ret['pages']
            not_nav_list = []
            for page in pages:
                if 'navigation' in page and not page['navigation']:
                    not_nav_list.append(page)
                else:
                    if 'sections' in page:
                        page.pop('sections')
            for not_nav in not_nav_list:
                pages.remove(not_nav)
            pages.sort(key=self._order_sort)
        return ret

    def _order_sort(self, val):
        return val["order"]


class CookiesSnackbarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CookiesSnackbar
        fields = ['title', 'info_text', 'accept_button_label', 'cookies_preferences_link_label']


class CookiesPreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CookiesPreferences
        fields = ['title', 'info_text', 'save_button_label',
                  'reject_all_button_label', 'accept_all_button_label']
