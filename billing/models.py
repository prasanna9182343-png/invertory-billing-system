from django.db import models
from django.core.validators import MinValueValidator
from customers.models import Customer
from inventory.models import Product

class Sale(models.Model):
    PAYMENT_CHOICES = [("CASH", "Cash"), ("CARD", "Card"), ("UPI", "UPI"), ("OTHER", "Other")]
    invoice_number = models.CharField(max_length=30, unique=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="sales", null=True, blank=True)
    payment_method = models.CharField(max_length=8, choices=PAYMENT_CHOICES, default="CASH")
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.invoice_number and self.pk is None:
            super().save(*args, **kwargs)
            self.invoice_number = f"INV-{self.created_at:%Y%m%d}-{self.pk:05d}"
            return super().save(update_fields=["invoice_number"])
        return super().save(*args, **kwargs)
    def __str__(self): return self.invoice_number or f"Sale {self.pk}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self): return f"{self.product} x {self.quantity}"
