from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('accounts/login/', LoginPage.as_view(), name='Login'),
    path('account/', login_required(SessionPage.as_view()), name='Session'),
    path('register/', register, name="Register")
]
