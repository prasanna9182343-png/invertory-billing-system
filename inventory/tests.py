from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Product

class ProductModelTests(TestCase):
    def test_product_string(self):
        category = Category.objects.create(name="Stationery")
        product = Product.objects.create(name="Pen", sku="PEN-01", category=category,
                                         purchase_price="5.00", selling_price="10.00", quantity=10)
        self.assertEqual(str(product), "Pen (PEN-01)")

class LoginProtectionTests(TestCase):
    def test_product_list_requires_login(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 302)
