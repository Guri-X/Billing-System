from django.db import models

class AddCustomer(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_contact = models.CharField(max_length=10)
    
    def __str__(self):
        return self.customer_name
