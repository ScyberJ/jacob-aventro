from django import forms
from general.models import Enquiry 


class ContactForm(forms.ModelForm):
    class Meta:
        exclude = ['id']
        model = Enquiry
    


