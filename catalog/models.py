from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название товара'
        verbose_name_plural = 'Названия товаров'
        ordering = ['id']
