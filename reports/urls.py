from django.urls import path
from . import views
urlpatterns = [path('', views.report_home, name='report_home'), path('sales.csv', views.export_sales_csv, name='export_sales_csv')]
