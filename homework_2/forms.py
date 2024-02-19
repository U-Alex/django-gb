from django import forms
# from django.forms import ModelForm
from .models import Product


class EditProductForm(forms.ModelForm):
    name = forms.CharField(label='название', max_length=30, widget=forms.TextInput(attrs={'size': 41}))
    description = forms.CharField(label='описание', widget=forms.Textarea(attrs={'cols': 41, 'rows': 8}))
    price = forms.DecimalField(label='цена', decimal_places=2, max_digits=8, min_value=1)
    quantity = forms.IntegerField(label='количество', min_value=1)
    image = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']

