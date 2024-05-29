from django.http import HttpResponse
from django.template import loader

def saludo(request):
    return HttpResponse('Hola LEANDRO VISTA')

