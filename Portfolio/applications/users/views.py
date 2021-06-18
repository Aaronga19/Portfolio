from django.shortcuts import render

from django.views.generic import CreateView
from .forms import ContactForm
# Create your views here.



class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = "users/contact.html"
    success_url = "."
    
