from django.forms import ModelForm
from .models import AddCustomer

class CustomerForm(ModelForm):
    class Meta:
        model = AddCustomer
        fields = '__all__'
