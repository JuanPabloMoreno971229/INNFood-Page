import uuid, os
from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=200, verbose_name="Título")
    autor= models.CharField(max_length=100, verbose_name="Autor")
    link=models.URLField(verbose_name="Enlace del artículo")   
    image= models.ImageField(verbose_name="Imagen", upload_to="blog")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["-created"]
    def __str__(self):
        return self.title
    def link_formated(self):
        new_link = self.link
        new_link = new_link.replace("view","preview") 
        print(new_link)
        return new_link