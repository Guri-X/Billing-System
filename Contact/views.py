from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse
from .models import ContactForm
from django.urls import reverse_lazy

class ContactPage(CreateView):
    template_name = 'contact.html'
    model = ContactForm
    fields = '__all__'
    success_url = reverse_lazy('Success')
