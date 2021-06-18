from django import forms
from django.forms import fields

#
from .models import UserContact

class ContactForm(forms.ModelForm):
    """ContactForm definition."""

    
    class Meta:
        model = UserContact
        fields= ('__all__')
