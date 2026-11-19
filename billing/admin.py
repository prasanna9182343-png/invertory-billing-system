from django.contrib import admin
from .models import Sale, SaleItem
class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 0
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "customer", "grand_total", "payment_method", "created_at")
    inlines = [SaleItemInline]
admin.site.register(SaleItem)
