from modeltranslation.translator import TranslationOptions, register

from .models import Category


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "short_description",
        "description",
    )
    hide_original = True
