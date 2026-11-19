from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, StockMovement
from .forms import ProductForm, CategoryForm

@login_required
def product_list(request):
    q = request.GET.get("q", "").strip()
    products = Product.objects.select_related("category").order_by("name")
    if q: products = products.filter(Q(name__icontains=q) | Q(sku__icontains=q) | Q(category__name__icontains=q))
    return render(request, "inventory/product_list.html", {"products": products, "q": q})

@login_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save()
        if product.quantity:
            StockMovement.objects.create(product=product, movement_type="IN", quantity=product.quantity, note="Opening stock")
        messages.success(request, "Product created successfully.")
        return redirect("product_list")
    return render(request, "form.html", {"form": form, "title": "Add product"})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, "Product updated.")
        return redirect("product_list")
    return render(request, "form.html", {"form": form, "title": "Edit product"})

@login_required
def category_list(request):
    categories = Category.objects.all().order_by("name")
    return render(request, "inventory/category_list.html", {"categories": categories})

@login_required
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request, "form.html", {"form": form, "title": "Add category"})
