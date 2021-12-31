from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from .models import AddCustomer
from .forms import CustomerForm
from django.urls import reverse_lazy
from .forms import ReportForm

class AddSalesView(CreateView):
     template_name = 'addsales.html'
     form_class = CustomerForm     
     success_url = reverse_lazy('Add_Sales')

class SalesDetailsView(TemplateView):
    template_name = 'salesdetails.html'

def create_sales_report(customer, products):
     pass

def generate_sales_report(request):
     context = {}
     form = ReportForm(request.POST or None)
     if request.method == "POST":
          if form.is_valid():
               customer = form.cleaned_data.get('customer')
               products = form.cleaned_data.get('products')
               create_sales_report(customer,products)
               return render(request,'generate_sales_report.html')
     context['form']=form
     return render(request,'generate_sales_report.html', context)
