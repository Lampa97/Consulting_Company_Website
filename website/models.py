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
            if self.pk:
                # Обновление существующего объекта
                old = Category.objects.get(pk=self.pk)
                if old.order_number != self.order_number:
                    if self.order_number < old.order_number:
                        # Сдвигаем вверх все между новым и старым (включительно новый, не включая старый)
                        Category.objects.filter(
                            order_number__gte=self.order_number,
                            order_number__lt=old.order_number
                        ).exclude(pk=self.pk).order_by('-order_number').update(order_number=models.F('order_number') + 1)
                    else:
                        # Сдвигаем вниз все между старым и новым (включительно старый, не включая новый)
                        Category.objects.filter(
                            order_number__gt=old.order_number,
                            order_number__lte=self.order_number
                        ).exclude(pk=self.pk).order_by('order_number').update(order_number=models.F('order_number') - 1)
            else:
                # Новый объект: сдвигаем только если есть конфликт
                conflict = Category.objects.filter(order_number=self.order_number)
                if conflict.exists():
                    total = Category.objects.count() + 1
                    qs = Category.objects.filter(order_number__gte=self.order_number, order_number__lte=total)
                    for cat in qs.order_by('-order_number'):
                        cat.order_number += 1
                        cat.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
