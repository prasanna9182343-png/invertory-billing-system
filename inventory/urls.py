from django.urls import path
from . import views
urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("add/", views.product_create, name="product_create"),
    path("<int:pk>/edit/", views.product_edit, name="product_edit"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/add/", views.category_create, name="category_create"),
]
