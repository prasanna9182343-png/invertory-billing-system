from django import forms
from .models import Product, Category
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "sku", "category", "description", "purchase_price", "selling_price", "quantity", "low_stock_threshold", "image"]
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
