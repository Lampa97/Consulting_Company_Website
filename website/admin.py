from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import translation
from .models import Category


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("title", "short_description", "slug")
    search_fields = ("title", "slug")
