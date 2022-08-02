from django import forms
from django.contrib.auth.models import User
from .models import Product


class UpdateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'category': 'Категории',
            'name': 'Название ',
            'price': "Цена",
            "img": "Изображение",
            'description': 'Описание ',
            'remainder': 'Остаток',

        }
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            "img": forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'remainder': forms.TextInput(attrs={'class': 'form-control'}),
        }
