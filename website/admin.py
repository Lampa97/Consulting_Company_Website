from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "slug")
    search_fields = ("title", "slug")
