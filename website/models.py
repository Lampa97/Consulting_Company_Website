from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, unique=True, max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to="category_backgrounds/")
    image = models.ImageField(upload_to="category_images/")
    order_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.order_number is not None:
            qs = Category.objects.filter(order_number__gte=self.order_number)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                # Сдвигаем все order_number >= текущего на 1
                for cat in qs.order_by('-order_number'):
                    cat.order_number += 1
                    cat.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
