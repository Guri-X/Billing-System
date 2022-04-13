from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from .models import AddProduct
from django.urls import reverse_lazy

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class AddProductView(CreateView):
    template_name = 'addproduct.html'
    model = AddProduct
    fields = '__all__'
    success_url = reverse_lazy('Product_Details')

class EditDetails(UpdateView):
    template_name = 'editdetails.html'
    model = AddProduct
    fields = '__all__'
    success_url = reverse_lazy('Product_Details')

class DeleteDetails(DeleteView):
    template_name = 'deletedetails.html'
    model = AddProduct
    fields = '__all__'
    success_url = reverse_lazy('Product_Details')

def product_details_view(request):
    prod = AddProduct.objects.all()
    context = {
        'product' : prod,
            }
    return render(request, "productdetails.html", context)

def logoutHandle(request):
    logout(request)
    return redirect('/')

def change_password(request):
    return render(request, "change_password.html")