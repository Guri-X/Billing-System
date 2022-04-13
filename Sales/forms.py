from django import forms
from .models import AddCustomer
from Dashboard.models import AddProduct

class CustomerForm(forms.ModelForm):
    class Meta:
        model = AddCustomer
        fields = '__all__'

class ReportForm(forms.Form):
    product_names = ((i.product_name, i.product_name) for i in AddProduct.objects.all().order_by('product_name'))
    customer = forms.ModelChoiceField(queryset=AddCustomer.objects.all().order_by('customer_name'))
    products = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=product_names)
    company_name = forms.CharField(max_length=500)
    company_address = forms.CharField(max_length=500)
    company_phone_number = forms.CharField(max_length=500)
    company_email_address = forms.CharField(max_length=500)

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        product_choices = self.get_product_choices()
        self.fields['products'].choices = self.get_product_choices()
        for prod in product_choices:
            self.fields[prod[0] + " quantity"] = forms.CharField(max_length=500)

    def get_product_choices(self):
        choices = ((i.product_name, i.product_name) for i in AddProduct.objects.all().order_by('product_name'))
        return choices