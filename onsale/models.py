from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.utils.timezone import now
import os
from django.utils.html import format_html

# Create your models here.
class Agentes(models.Model):
    name=models.CharField(null=False,max_length= 100)
    lastname=models.CharField(null=False,max_length= 100)
    phone=models.IntegerField()
    email= models.EmailField()
    pic=models.ImageField(upload_to="fotos", null=True)
    about=models.CharField(null=True,max_length= 200)
    instagram=models.URLField(null=True, max_length=200)
    twiter=models.URLField(null=True,blank=True, max_length=200)
    facebook=models.URLField(null=True,blank=True, max_length=200)
    linkedin=models.URLField(null=True, blank=True,max_length=200)
    
    def delete(self,*args, **kwargs):
        if os.path.isfile(self.pic.path):
            os.remove(self.pic.path)           
        super(Agentes,self).delete(*args, **kwargs)
    

    def __str__(self):
        return f'Nombre: {self.name} - Apellido: {self.lastname}'

    
class Houses(models.Model):
    lugar=models.CharField(null=False,max_length=100)
    foto=models.ImageField(upload_to="fotos", null=True)
    foto2=models.ImageField(upload_to="fotos", null=True)
    foto3=models.ImageField(upload_to="fotos", null=True)
    direccion=models.IntegerField()
    precio=models.IntegerField(null=True)
    beds=models.IntegerField(null=True)
    baths=models.IntegerField(null=True)
    description=models.TextField(null=True,max_length=500)
    Agente=models.ForeignKey(Agentes,null=True, blank=True, on_delete=models.CASCADE)
    
    def delete(self,*args, **kwargs):
        if os.path.isfile(self.foto.path):
            os.remove(self.foto.path)
            os.remove(self.foto2.path) 
            os.remove(self.foto3.path)                    
        super(Houses,self).delete(*args, **kwargs)           
    def __str__(self):
        return f'Calle: {self.lugar}-Direccion: {self.direccion}-Precio: {self.precio}'
       

class Contacto(models.Model):
    contact_nombre=models.CharField(null=False,max_length=100)
    correo=models.EmailField(max_length=254,null=False)
    mensaje=models.TextField(null=True,max_length=250)
    create_date=models.DateTimeField(default=now, editable=False)
    
    def __str__(self):
        return self.contact_nombre
    
    



    

# class Onsale(models.Model):
    
#     calle=models.CharField(null=True,max_length=100)
#     foto=models.CharField(max_length=100)
#     foto2=models.ImageField(upload_to="fotos", null=True)
#     foto3=models.ImageField(upload_to="fotos", null=True)
#     direccion=models.IntegerField()
#     Agente=models.ForeignKey(Agentes,null=True, blank=True, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return  f'Calle: {self.calle}-Direccion: {self.direccion}'
    
# class Products(models.Model):
#     adress=models.CharField(null=False,max_length=100)
#     pic=models.ImageField(upload_to="fotos", null=True)
#     pic2=models.ImageField(upload_to="fotos", null=True)
#     pic3=models.ImageField(upload_to="fotos", null=True)
#     areacode=models.IntegerField()
#     price=models.IntegerField(null=True)
#     beds=models.IntegerField(null=True)
#     baths=models.IntegerField(null=True)
#     def __str__(self):
#         return self.adress