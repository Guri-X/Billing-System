from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class AddProductView(TemplateView):
    template_name = 'addproduct.html'
