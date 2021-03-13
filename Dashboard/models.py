from django.db import models
from django.urls import reverse

class AddProduct(models.Model):
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    product_cost = models.CharField(max_length=100)
    product_company = models.CharField(max_length=100)
    product_stock = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('edit_details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.product_name
