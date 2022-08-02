from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'price', 'remainder']
    list_filter = ['remainder']
    list_editable = ['price', 'remainder']

