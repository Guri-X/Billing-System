from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('contact/', contactPage, name='Contact'),
    path('success/', successPage, name='Success'),
]
