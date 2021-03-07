from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class LoginPage(TemplateView):
    template_name = 'login.html'

class SessionPage(TemplateView):
    template_name = 'logged_in.html'
