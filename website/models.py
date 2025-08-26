from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, unique=True, max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to="category_backgrounds/")
    image = models.ImageField(upload_to="category_images/")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
