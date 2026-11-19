import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from billing.models import Sale

@login_required
def report_home(request):
    sales = Sale.objects.select_related("customer").order_by("-created_at")
    start = request.GET.get("start", "")
    end = request.GET.get("end", "")
    if start: sales = sales.filter(created_at__date__gte=start)
    if end: sales = sales.filter(created_at__date__lte=end)
    return render(request, "reports/home.html", {"sales": sales, "start": start, "end": end})

@login_required
def export_sales_csv(request):
    sales = Sale.objects.select_related("customer").order_by("-created_at")
    start, end = request.GET.get("start", ""), request.GET.get("end", "")
    if start: sales = sales.filter(created_at__date__gte=start)
    if end: sales = sales.filter(created_at__date__lte=end)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="sales_report.csv"'
    writer = csv.writer(response)
    writer.writerow(["Invoice", "Customer", "Date", "Payment", "Subtotal", "Discount", "Tax %", "Grand Total"])
    for sale in sales:
        writer.writerow([sale.invoice_number, sale.customer or "Walk-in", sale.created_at, sale.payment_method,
                         sale.subtotal, sale.discount, sale.tax_percent, sale.grand_total])
    return response
