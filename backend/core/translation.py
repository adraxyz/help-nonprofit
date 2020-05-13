from modeltranslation.translator import register, TranslationOptions
from .models import Message, Label


@register(Message)
class MessageTranslationOptions(TranslationOptions):
    fields = ('text_to_users',)


@register(Label)
class LabelTranslationOptions(TranslationOptions):
    fields = ('label',)
