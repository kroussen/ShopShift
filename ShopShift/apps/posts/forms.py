from django import forms
from .models import Product
from decimal import Decimal


class ProductCreationForm(forms.ModelForm):
    title = forms.CharField(label='Название продукта')
    price = forms.DecimalField(label='Цена продукта', min_value=Decimal('0.00'))

    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 70, 'rows': 10, 'id': 'description'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')

        # Ensure that price is a valid Decimal object
        if not isinstance(price, Decimal):
            raise forms.ValidationError('Введите корректное числовое значение для цены.')

        return price
