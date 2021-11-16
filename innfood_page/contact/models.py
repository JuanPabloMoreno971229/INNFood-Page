from django.db import models
from tkinter import *
from django.forms import fields
from django.forms.fields import ChoiceField

# Create your models here.
class Contact(models.Model):
   
    procedure=models.CharField(max_length=200, null=True, verbose_name="Procedimiento", choices= (
        ('P', 'Peticiones'),
        ('Q', 'Quejas'),
        ('R', 'Reclamos'),
        ('S', 'Sugerencias'),
    ))
    name= models.CharField(max_length=200, null=False, verbose_name="Nombre")
    mail= models.EmailField(max_length=200, null=False, verbose_name="Correo electrónico")
    phone= models.CharField(max_length=200, null=False, verbose_name="Número de teléfono")
    message= models.TextField(verbose_name="Mensaje")
    status=models.BooleanField(default=False, verbose_name="Contestado")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["-created"]
        HIDDEN
                
    def __str__(self):
        return self.name

  