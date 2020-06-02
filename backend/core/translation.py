from modeltranslation.translator import register, TranslationOptions
from .models import Message, Label, CookiesProvider, CookiesCategory, Cookie


@register(Message)
class MessageTranslationOptions(TranslationOptions):
    fields = ('text_to_users',)


@register(Label)
class LabelTranslationOptions(TranslationOptions):
    fields = ('label',)


@register(CookiesCategory)
class CookiesCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CookiesProvider)
class CookiesProviderTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Cookie)
class CookieTranslationOptions(TranslationOptions):
    fields = ('title', 'purpose', 'duration')
