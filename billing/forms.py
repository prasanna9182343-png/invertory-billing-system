from django import forms
from customers.models import Customer
from inventory.models import Product
from .models import Sale
class SaleForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=False)
    product = forms.ModelChoiceField(queryset=Product.objects.filter(quantity__gt=0))
    quantity = forms.IntegerField(min_value=1, initial=1)
    discount = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2, initial=0, required=False)
    tax_percent = forms.DecimalField(min_value=0, max_value=100, max_digits=5, decimal_places=2, initial=0, required=False)
    payment_method = forms.ChoiceField(choices=Sale.PAYMENT_CHOICES)
