from django.db import models
from django.db.models.fields import CharField, PositiveBigIntegerField

# Create your models here.

class visitas(models.Model):

    sitio_web = CharField(max_length=255, default="")
    contador = PositiveBigIntegerField(default=0)
    fecha = CharField(max_length=10, default="")
    def __str__(self):
        return "Pagina: {}".format(self.sitio_web)
