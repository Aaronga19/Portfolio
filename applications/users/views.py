from django.shortcuts import render

from django.core.mail import send_mail

from django.views.generic import CreateView
from .forms import ContactForm
from django.http import HttpResponseRedirect
# Create your views here.



class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = "users/contact.html"
    success_url = "."
    
    
    
    def form_valid(self,form):
        
        name = self.request.POST['name']
        email = self.request.POST['email']
        phone = self.request.POST['phone']
        company = self.request.POST['company']
        message = self.request.POST['message'] + f'\n\n My phone number is: {phone} and you can keep in touch with me in {email}'
        officialMail = 'Mett Inc.'
        destiny = ["arcanmett@gmail.com"]
        subject = f"You have just recieved a message by {name} from {company}, who want to be in contact with you"

        send_mail(subject, message, officialMail, destiny)
        
        return super(ContactCreateView, self).form_valid(form)
        
