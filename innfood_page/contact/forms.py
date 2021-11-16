from tkinter import Label
from django import forms
from django.forms import widgets 
from .models import Contact


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'procedure': forms.Select(attrs={'class':'contact-form-text','placeholder':'Tipo de solicitud'}),
            'name' : forms.TextInput(attrs={'class':'contact-form-text','placeholder':'Nombre'}),
            'mail' : forms.EmailInput(attrs={'class':'contact-form-text','placeholder':'Correo'}),
            'phone' : forms.TextInput(attrs={'class':'contact-form-text','placeholder':'Teléfono'}),
            'message' : forms.TextInput(attrs={'class':'contact-form-text','placeholder':'Mensaje'}),
            'status' : forms.HiddenInput(attrs={'class':'contact-form-text','placeholder':'Estado'}),
        }
        labels = {'procedure': '','name': '', 'mail': '', 'phone': '', 'message': ''}
    
    
    

