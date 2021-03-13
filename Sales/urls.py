from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('add_sales/', AddSalesView.as_view(), name='Add_Sales'),
    path('sales_details/', SalesDetailsView.as_view(), name='Sales_Details'),
    ]
