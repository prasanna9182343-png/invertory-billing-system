from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", account_views.dashboard, name="dashboard"),
    path("products/", include("inventory.urls")),
    path("suppliers/", include("suppliers.urls")),
    path("customers/", include("customers.urls")),
    path("billing/", include("billing.urls")),
    path("reports/", include("reports.urls")),
]
