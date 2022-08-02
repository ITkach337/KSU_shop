from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models. Model):
    CUPS = 'cups'
    T_SHIRTS = 't_shirts'
    CAPS = 'caps'
    PENS = 'pens'

    CATEGORY_GROUP = {
        (CUPS, 'cups'),
        (T_SHIRTS, 't_shirts'),
        (CAPS, 'caps'),
        (PENS, 'pens')

    }
    category = models.CharField(blank=False, max_length=30, choices=CATEGORY_GROUP, verbose_name='Категории')
    name = models.CharField(blank=False, max_length=64, verbose_name='Название')
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False, verbose_name='Цена')
    description = models.TextField(null=True, verbose_name='Описание')
    remainder = models.BooleanField(default=0, blank=False, verbose_name='Остаток')
    img = models.ImageField(upload_to='product_img', blank=True, verbose_name='Изображение')

    def __str__(self):
        return f'{self.name}'


