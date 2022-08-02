from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 15)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Кол-во',
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'min': '1',
                'value': '1',

            }
        )
    )

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

