from django.db import models
from apps.users.models import CustomUser


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')
    description = models.TextField(verbose_name='Описание продукта')
    image = models.URLField(blank=True, null=True, verbose_name='Изображение продукта')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор объявления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
