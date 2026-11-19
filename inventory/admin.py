from django.contrib import admin
from .models import Category, Product, StockMovement
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category", "selling_price", "quantity", "low_stock_threshold")
    list_filter = ("category",)
    search_fields = ("name", "sku")
@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ("product", "movement_type", "quantity", "created_at")
