from django.urls import path
from .views import DashboardView, AddProductView, product_details_view, EditDetails, DeleteDetails, logoutHandle

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('add_product/', AddProductView.as_view(), name='Add_Product'),
    path('product_details/', product_details_view, name='Product_Details'),
    path('<int:pk>/edit_details/', EditDetails.as_view(), name='Edit_Details'),
    path('<int:pk>/delete_details/', DeleteDetails.as_view(), name='Delete_Details'),
    path('logout/', logoutHandle, name='Logout'),
]
