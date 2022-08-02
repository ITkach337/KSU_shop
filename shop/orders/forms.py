from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'address': 'Адрес',
            'postal_code': 'Индекс',
            'city': 'Город'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
            'address': forms.TextInput(attrs={'placeholder': 'Введите адрес'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите эл.адрес'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'индекс'}),
            'city': forms.TextInput(attrs={'placeholder': 'Введите город'}),
        }
