from rest_framework import serializers
from ..models import (Layout, Page, Section, Text, Image, Video,
                      Button, Footer, Socials, Document)


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = ['order', 'title', 'subtitle', 'content', 'project_section']


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['order', 'content', 'alt_content', 'alt', 'project_section']


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


class ButtonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Button
        fields = ['order', 'to', 'text_0', 'text_1', 'href', 'target', 'project_section']


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ['order', 'title', 'subtitle', 'description', 'file', 'project_section']


class SectionSerializer(serializers.ModelSerializer):
    texts = TextSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    buttons = ButtonSerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['texts', 'images', 'videos', 'buttons', 'documents',
                  'order', 'title', 'subtitle']


class PageSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['order', 'name', 'title', 'navigation', 'sections']
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
        model = Socials
        fields = '__all__'


class LayoutSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)
    logo = ImageSerializer(read_only=True)
    donation_button = ButtonSerializer(read_only=True)
    contact_button = ButtonSerializer(read_only=True)
    footer = FooterSerializer(read_only=True)
    socials = SocialSerializer(read_only=True)

    class Meta:
        model = Layout
        fields = ['name', 'pages', 'logo', 'donation_button',
                  'contact_button', 'footer', 'socials', 'privacy_text']
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
