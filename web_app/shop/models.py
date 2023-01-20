from django.db import models
from django.urls import reverse



# Модели для интернет магазина shop

class Categories(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/%Y-%m-%d/", default="images/default.jpg")
    parent_id = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/%Y-%m-%d/", default="images/default.jpg")
    price = models.DecimalField(max_digits=15, decimal_places=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']
