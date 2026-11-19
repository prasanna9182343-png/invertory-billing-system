from django.db import models
class Supplier(models.Model):
    name = models.CharField(max_length=160)
    company = models.CharField(max_length=160, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name="purchases")
    reference = models.CharField(max_length=80, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Purchase #{self.pk} - {self.supplier}"
