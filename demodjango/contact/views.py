from django.shortcuts import render
from .forms import contact_Form 
from .models import ContactForm
from django.http import HttpResponse
from django.views import View
class contact(View):
    
    def get(self,request):
    
        cf = contact_Form

        # Render the contact.html template with the form instance in the context
        return render(request, 'contact/contact.html', {'cf': cf})
    def post(self,request):
        if request.method=="POST":
            cf = contact_Form(request.POST)
            if cf.is_valid():
                saveCF=ContactForm(username=cf.cleaned_data['username'],
                    email= cf.cleaned_data['email'],
                    body=  cf.cleaned_data['body'])
                saveCF.save()
                return HttpResponse('save success')
        else:
            return HttpResponse('error')    