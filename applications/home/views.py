from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from . forms import contactForm

# Create your views here.


class HomePage(TemplateView):
    template_name = "home/index.html"


class AboutMe(TemplateView):
    template_name = "home/me.html"



