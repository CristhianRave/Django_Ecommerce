from django.shortcuts import render, redirect
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.


def index(request):
    
    return render(request, 'index.html')


def contact(request):
    nombre = request.POST.get('nombre')
    email = request.POST.get('email')
    mensaje = request.POST.get('mensaje')
    
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            messages.info(request,"Gracias por contactarnos")
            
            #Enviamos los datos del formulario a nuestro mail           
            full_menssage = f"""
                Mensaje recibido de {nombre}, {email}
                ___________________________________
                {mensaje}
                """

            send_mail(
                subject="Mensaje recibido desde ContactForm",
                message=full_menssage,
                from_email= settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFY_EMAIL]    
            )
        
            return redirect('contact')

    return render(request, 'contact.html',{
        'form': form,
    })