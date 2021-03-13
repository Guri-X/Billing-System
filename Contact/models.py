from django.db import models

class ContactForm(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_contact = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=400)
    
    def __str__(self):
        return self.subject

