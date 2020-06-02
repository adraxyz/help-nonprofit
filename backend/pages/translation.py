from modeltranslation.translator import register, TranslationOptions
from .models import (Footer, Page, Button, Text, Section, Image, Document,
                     MetaTag, CookiesSnackbar, CookiesPreferences)


@register(Footer)
class FooterTranslationOptions(TranslationOptions):
    fields = ('footer_1_col_title', 'footer_2_col_title', 'footer_3_col_title',
              'registered_office', 'subscribe_btn_text', 'footer_1_col_text',
              'footer_2_col_text', 'footer_3_col_text', 'donation_title', 'transparency_title')


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'name')


@register(Section)
class SectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


@register(Button)
class ButtonTranslationOptions(TranslationOptions):
    fields = ('text_0', 'text_1')


@register(Text)
class TextTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')


@register(Image)
class ImageTranslationOptions(TranslationOptions):
    fields = ('content', 'alt_content', 'alt')


@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'file')


@register(MetaTag)
class MetaTagTranslationOptions(TranslationOptions):
    fields = ('content', )


@register(CookiesSnackbar)
class CookiesSnackbarTranslationOptions(TranslationOptions):
    fields = ('title', 'info_text', 'accept_button_label', 'cookies_preferences_link_label')


@register(CookiesPreferences)
class CookiesPreferencesTranslationOptions(TranslationOptions):
    fields = ('title', 'info_text', 'save_button_label',
              'reject_all_button_label', 'accept_all_button_label')
