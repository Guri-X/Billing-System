from django.urls import path
from .views import *

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='About'),
    path('', HomePageView.as_view(), name='Home'),
    path('contact/', ContactPageView.as_view(), name='Contact')
]
