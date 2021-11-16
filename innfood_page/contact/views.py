from .models import Contact
from django.shortcuts import redirect, render
from .forms import ContactoForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


# Create your views here.
def send_email(mail, name, procedure):
    context = {'name': name, 'procedure': procedure}
    template = get_template('contact/email.html')
    content = template.render(context)
    email = EmailMultiAlternatives(
        'INNFood',
        'SoyInnFood',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email_self = EmailMultiAlternatives(
        'INNFood',
        'SoyInnFood',
        settings.EMAIL_HOST_USER,
        ["pruebainnfood@gmail.com"]
    )
    email.attach_alternative(content, 'text/html')
    email.send()
    email_self.attach_alternative(content, 'text/html')
    email_self.send()

def contact(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        mail = request.POST.get('mail')
        name = request.POST.get('name')
        procedure = request.POST.get('procedure')
        if procedure == 'P':
            procedure = 'petición'
        elif procedure == 'Q':
            procedure = 'queja'
        elif procedure == 'R':
            procedure = 'reclamo'
        elif procedure == 'S':
            procedure = 'sugerencia'                 
        send_email(mail, name, procedure)
        if form.is_valid():
            form.save()
            return redirect('contacto')
    else:
        form = ContactoForm()

    context = {
        
        'form':form,
    }
    #contacts = Contact.objects.all() 
    return render(request, "contact/contact.html", context)


