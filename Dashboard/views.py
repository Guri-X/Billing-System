from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth import logout

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class AddProductView(TemplateView):
    template_name = 'addproduct.html'

def logoutHandle(request):
    logout(request)
    return redirect('/')
