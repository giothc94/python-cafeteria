from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form=ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            # envio de correo
            email = EmailMessage(
                subject="La Caffettiera",
                body="De {} <{}>\n\nEscribio:\n{}".format(name,email,content),
                from_email="no-contestar@mailtrap.com",
                to=["gio666nb@gmail.com"],
                reply_to=[email]
                )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?error')
    return render(request,'contact/contact.html',{"form_contact":contact_form})