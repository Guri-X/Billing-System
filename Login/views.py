from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginPage(TemplateView):
    template_name = 'login.html'

@method_decorator(login_required, name='dispatch')
class SessionPage(TemplateView):
    template_name = 'logged_in.html'
