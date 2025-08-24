from django import forms
from django.utils.text import slugify

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "title",
            "short_description",
            "description",
            "background_image",
            "image",
        ]

    def save(self, commit=True):
        self.instance.slug = slugify(self.instance.title)
        return super().save(commit)
