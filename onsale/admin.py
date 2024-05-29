from django.contrib import admin
from .models import  Houses,  Agentes, Contacto #, Onsale,Products,
from django.utils.html import format_html

# class Houses(admin.ModelAdmin): 
#     # def image_tag(self, obj):
#     #     return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
#     list_display=['lugar','direccion','foto','foto2','foto3']
    
class ImageHouses(admin.ModelAdmin):
    
    list_display=['lugar','foto',"image_tag"] 
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>',obj.foto.url)   

class ImageAgente(admin.ModelAdmin):
    
    list_display=['name','lastname',"image_tag"] 
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>',obj.pic.url)   


    
# Register your models here.
#admin.site.register(Onsale)
admin.site.register(Houses,ImageHouses)
#admin.site.register(Products)
admin.site.register(Agentes,ImageAgente)
admin.site.register(Contacto)


