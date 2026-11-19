from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from inventory.models import Product, StockMovement
from .models import Sale, SaleItem
from .forms import SaleForm

@login_required
def sale_list(request):
    return render(request, "billing/list.html", {"sales": Sale.objects.select_related("customer").order_by("-created_at")})

@login_required
def sale_create(request):
    form = SaleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        product = form.cleaned_data["product"]
        qty = form.cleaned_data["quantity"]
        discount = form.cleaned_data.get("discount") or Decimal("0")
        tax_percent = form.cleaned_data.get("tax_percent") or Decimal("0")
        with transaction.atomic():
            product = Product.objects.select_for_update().get(pk=product.pk)
            if qty > product.quantity:
                form.add_error("quantity", f"Only {product.quantity} units are available.")
            else:
                subtotal = product.selling_price * qty
                taxable = max(Decimal("0"), subtotal - discount)
                tax = taxable * tax_percent / Decimal("100")
                total = taxable + tax
                sale = Sale.objects.create(
                    customer=form.cleaned_data["customer"],
                    payment_method=form.cleaned_data["payment_method"],
                    discount=discount, tax_percent=tax_percent,
                    subtotal=subtotal, grand_total=total
                )
                SaleItem.objects.create(sale=sale, product=product, quantity=qty,
                                         unit_price=product.selling_price, line_total=subtotal)
                Product.objects.filter(pk=product.pk).update(quantity=F("quantity") - qty)
                StockMovement.objects.create(product=product, movement_type="OUT", quantity=qty,
                                             note=f"Sale {sale.invoice_number}")
                messages.success(request, f"Invoice {sale.invoice_number} created.")
                return redirect("sale_detail", pk=sale.pk)
    return render(request, "form.html", {"form": form, "title": "Create sale / bill"})

@login_required
def sale_detail(request, pk):
    sale = get_object_or_404(Sale.objects.select_related("customer").prefetch_related("items__product"), pk=pk)
    return render(request, "billing/detail.html", {"sale": sale})
