from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from .models import Contact

@csrf_exempt
def contactPage(request):
    if request.method == "POST":
        contact = Contact()
        username = request.POST.get('username')
        useremail = request.POST.get('email')
        usercontact = request.POST.get('contact')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.User_Name = username
        contact.from_email = useremail
        contact.User_Contact = usercontact
        contact.subject = subject
        contact.message = message
        contact.save()
        return HttpResponse("<h1>Thank you for contacting us.</h1>")

    return render(request, 'contact.html')

def successPage(TemplateView):
    template_name = 'success.html'

