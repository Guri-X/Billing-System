from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('add_product/', AddProductView.as_view(), name='Add_Product'),
    path('logout/', logoutHandle, name='Logout'),
]
