from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm
@login_required
def supplier_list(request):
    return render(request, "suppliers/list.html", {"suppliers": Supplier.objects.order_by("name")})
@login_required
def supplier_create(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("supplier_list")
    return render(request, "form.html", {"form": form, "title": "Add supplier"})
