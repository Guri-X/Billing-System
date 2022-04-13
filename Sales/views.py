import datetime
import enum
from unicodedata import name
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from .models import AddCustomer
from Dashboard.models import AddProduct
from .forms import CustomerForm
from django.urls import reverse_lazy
from .forms import ReportForm
import io
from reportlab.pdfgen import canvas
from django.http import FileResponse
import string
import random
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

class AddSalesView(CreateView):
     template_name = 'addsales.html'
     form_class = CustomerForm     
     success_url = reverse_lazy('Add_Sales')

class SalesDetailsView(TemplateView):
    template_name = 'salesdetails.html'

def create_sales_report(customer, products, company_name, company_address, company_phone_number, company_email_address, prod_quantity):
     customer_details = AddCustomer.objects.get(customer_name=customer)
     product_details = []
     for i in products:
          temp_details = AddProduct.objects.get(product_name=i)
          product_details.append(temp_details)
     buffer = io.BytesIO()
     p = canvas.Canvas(buffer)
     invoice_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))

     p.drawString(250, 780, "Billing System Invoice")
     p.drawString(15, 720, f"Company Name: {company_name}")
     p.drawString(15, 700, f"Company Address: {company_address}")
     p.drawString(15, 680, f"Company Phone Number: {company_phone_number}")
     p.drawString(15, 660, f"Company Email Address: {company_email_address}")

     p.drawImage("/home/guri/Projects/Billing_System/static/img/invoice-logo.jpg", 400, 650, 100, 100)

     p.drawString(15, 600, "Customer Details")
     p.line(15, 597, 107, 597)
     p.drawString(15, 580, f"Customer Name: {customer_details.customer_name}")
     p.drawString(15, 560, f"Customer Phone Number: {customer_details.customer_contact}")

     p.drawString(395, 600, f"Invoice No.: {invoice_number}")
     p.drawString(395, 580, f"Date: {datetime.datetime.now().date()}")
     p.drawString(395, 560, f"Time: {datetime.datetime.now().time()}")

     p.drawString(15, 500, "Product Details")
     p.line(15, 497, 97, 497)

     data = [("Product Name", "Product Type", "Product Cost", "Product Quantity", "Total Amount")]
     for index,prod in enumerate(product_details):
          qty = prod_quantity[index]
          cost = prod.product_cost
          total = int(qty) * float(cost)
          temp_data = (prod.product_name, prod.product_type, cost, qty, total)
          data.append(temp_data)
     prod_table = Table(data, colWidths=[150, 150, 80, 90, 80])
     prod_table.setStyle(TableStyle([
          ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
          ('BOX', (0,0), (-1,-1), 0.25, colors.black)
     ]))
     prod_table.wrapOn(p, 100, 100)
     prod_table.drawOn(p, 15, 450)

     p.setFillColorRGB(235, 64, 52)
     p.rect(15,15,567,20, stroke=1, fill=1)
     p.setFillColorRGB(235, 64, 52)
     p.rect(15,805,567,20, stroke=1, fill=1)

     p.showPage()
     p.save()
     buffer.seek(0)
     file_name = f"Invoice-{str(datetime.datetime.now())}.pdf" 

     return FileResponse(buffer, as_attachment=True, filename=file_name)

def generate_sales_report(request):
     context = {}
     form = ReportForm(request.POST or None)
     if request.method == "POST":
          if form.is_valid():
               customer = form.cleaned_data.get('customer')
               products = form.cleaned_data.get('products')
               company_name = form.cleaned_data.get("company_name")
               company_address = form.cleaned_data.get("company_address")
               company_phone_number = form.cleaned_data.get("company_phone_number")
               company_email_address = form.cleaned_data.get("company_email_address")
               prod_quantity = []
               for i in products:
                    temp_quantity = form.cleaned_data.get(i + " quantity")
                    prod_quantity.append(int(temp_quantity))
               sales_report = create_sales_report(customer, products, company_name, company_address, company_phone_number, company_email_address, prod_quantity)
               return sales_report
     context['form']=form
     return render(request,'generate_sales_report.html', context)
