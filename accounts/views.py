from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from inventory.models import Product
from customers.models import Customer
from billing.models import Sale
from django.db.models import Sum, F
from django.utils import timezone
from datetime import timedelta

@login_required
def dashboard(request):
    today = timezone.localdate()
    sales_today = Sale.objects.filter(created_at__date=today).aggregate(total=Sum("grand_total"))["total"] or 0
    context = {
        "product_count": Product.objects.count(),
        "customer_count": Customer.objects.count(),
        "sales_count": Sale.objects.count(),
        "sales_today": sales_today,
        "low_stock": Product.objects.filter(quantity__lte=F("low_stock_threshold")).order_by("quantity")[:8],
        "recent_sales": Sale.objects.select_related("customer").order_by("-created_at")[:6],
    }
    return render(request, "dashboard.html", context)
