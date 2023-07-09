from django import forms
from .models import Contact_us

class FormContactForm(forms.ModelForm):
    class Meta:
        model= Contact_us
        fields= ["name", "email", "phone_number", "message"]