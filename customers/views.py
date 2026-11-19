from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
@login_required
def customer_list(request):
    return render(request, "customers/list.html", {"customers": Customer.objects.order_by("name")})
@login_required
def customer_create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("customer_list")
    return render(request, "form.html", {"form": form, "title": "Add customer"})
