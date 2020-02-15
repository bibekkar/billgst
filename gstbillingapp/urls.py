from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('invoices', views.invoices, name='invoices'),
    path('customers', views.customers, name='customers'),
    path('customers/add', views.customer_add, name='customer_add'),
    path('customers/edit/<int:customer_id>', views.customer_edit, name='customer_edit'),
    path('customers/delete', views.customer_delete, name='customer_delete'),
    path('customersjson', views.customersjson, name='customersjson'),

    path('products', views.products, name='products'),
    path('products/add', views.product_add, name='product_add'),
    path('products/edit/<int:product_id>', views.product_edit, name='product_edit'),
    path('products/delete', views.product_delete, name='product_delete'),

    path('productsjson', views.productsjson, name='productsjson'),

    path('invoice/<int:invoice_id>', views.invoice_viewer, name='invoice_viewer'),
]