from django.db import models

class Contact(models.Model):
    User_Name = models.CharField(max_length=200)
    from_email = models.EmailField()
    User_Contact = models.IntegerField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name

