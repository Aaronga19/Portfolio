from django import forms
from django.forms import fields

#
from .models import UserContact

class ContactForm(forms.ModelForm):
    """ContactForm definition."""

    
    class Meta:
        model = UserContact
        fields= ('__all__')
        widgets = {
            'name': forms.TextInput(
                attrs={
                'placeholder':'Full Name',
                'class':'form-control',
                'type':'text',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                'placeholder':'E-Mail',
                'class':'form-control', 
                }
            ),
            'phone': forms.TextInput(
                attrs={
                'placeholder':'Phone Number',
                'class':'form-control',
                'type':'text',
                }
            ),
            'company': forms.TextInput(
                attrs={
                'placeholder':'Company or Personal?',
                'class':'form-control',
                'type':'text',
                }
            ),
            'message': forms.Textarea(
                attrs={
                'placeholder':'Let me know how I can help you ☺',
                'class':'form-control',
                'aria-label':"With textarea",
                }
            ),
            
        }
