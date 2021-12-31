from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class LoginPage(TemplateView):
    template_name = 'login.html'

class SessionPage(TemplateView):
    template_name = 'logged_in.html'

def register(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'logged_in.html')
    context['form']=form
    return render(request,'register.html',context)
