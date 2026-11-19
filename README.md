# Inventory and Billing Management System

A Django starter application for a diploma final-year project. It includes product/category management, customers, suppliers, purchases, sales, stock movements, a dashboard, CSV reports, and printable invoice pages.

## Requirements
- Python 3.10+
- macOS Terminal (also works on other operating systems)
- SQLite is configured by default; MySQL is not required for local development.

## Setup on macOS

```bash
cd inventory_billing
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the app and http://127.0.0.1:8000/admin/ for Django admin.

## Important first steps
1. Create a superuser and sign in.
2. Add categories, products, customers, and suppliers using Django admin at `/admin/`.
3. Use `/products/`, `/customers/`, `/suppliers/`, and `/billing/` to explore the app.
4. Run tests with `python manage.py test`.

## Project apps
- `accounts`: login and dashboard routing
- `inventory`: categories, products, stock movements
- `suppliers`: supplier and purchase records
- `customers`: customer records
- `billing`: sales and sale items
- `reports`: CSV sales report

## Notes
This is a working educational starter project, not a production-ready accounting system. Payment gateway integration, barcode scanning, multi-warehouse stock, tax compliance, audit logging, and production deployment hardening are not included. Review tax and invoice requirements with your college before submitting.
