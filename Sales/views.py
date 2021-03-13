from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from .models import AddCustomer
from .forms import CustomerForm
from django.urls import reverse_lazy

class AddSalesView(CreateView):
     template_name = 'addsales.html'
     form_class = CustomerForm     
     success_url = reverse_lazy('Add_Sales')

class SalesDetailsView(TemplateView):
    template_name = 'salesdetails.html'
