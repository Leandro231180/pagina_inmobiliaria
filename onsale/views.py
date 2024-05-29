from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Houses, Agentes, Contacto #, Onsale, Products
from .forms import CreateNewSale, ContactoForm, UserRegistroForm,EditRegistroForm,PasswordCambioForm, AgentesForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.detail import DetailView
from django.db.models import Q
import datetime
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
import re



def index(request):
    ventas = Houses.objects.all()
    agentes=Agentes.objects.all()
    return render(request,'index.html', {'ventas': ventas, "agentes":agentes})



def allproperties(request):
    ventas = Houses.objects.all()
    return render(request,'properties.html', {'ventas': ventas})


def padre(request):
    ventas = Houses.objects.all()
    print(request.GET)
    return render(request, "padre.html", {'ventas': ventas})


class Formulario(CreateView):
    model = Houses
    form_class = CreateNewSale
    template_name = 'prueba3.html'
    
    def form_valid(self, form):
        
        return super().form_valid(form)

    
class ListaCasasGeek(CreateView):
    model=Houses
    #fields=["lugar","foto","direccion","precio","beds","baths","description", "Agente"]
    form_class= CreateNewSale
    
    template_name="houses_form.html"
    success_url = 'allprop'
 
class ListaCasasGeek2(CreateView):
    model=Houses
    #fields=["lugar","foto","direccion","precio","beds","baths","description", "Agente"]
    form_class= CreateNewSale
    
    template_name="houses_form copy.html"
    success_url = 'allprop'    
    
def hija(request):
    ventas = Houses.objects.all()
    return render(request, "hija.html", {'ventas': ventas})
        

def listaprop(request):
    ventas = Houses.objects.all()
    return render(request, "proplist.html", {'ventas': ventas})
    
class ModPublication(UpdateView):
    model=Houses
    fields=["lugar","foto","foto2","foto3","direccion","precio","beds","baths","description","Agente"]
    template_name="update_form.html"
    success_url = '/allprop'

    
class HomeDetail(DetailView):
    template_name= "detallesales.html"
    queryset= Houses.objects.all()
    
def listar_todas(request):
    ventas = Houses.objects.all()
    return render(request,'buscar_listar.html', {'ventas': ventas})

    
class ProductDetailView(DetailView):
    model=Houses
    context_object_name = "houses_det"
    template_name="detallesales.html"  
             
                     
def busqueda_Prop(request):    
    return render(request, "buscar.html")   


def search(request):
    lugar=request.GET.get("lugar")
    
    if lugar:
        find_home= Houses.objects.filter(Q(lugar__icontains=lugar) | Q(direccion__icontains=lugar)| Q(precio__icontains=lugar)) 
        return render(request,"result_search.html",{"respuesta":find_home, "lugar":lugar,})
    else: 
        respuesta= "no enviaste un dato valido Salame"
        return render(request,"result_search.html",{})
    
    
def search_father(request):
    if request.GET["lugar"]:
         lugar= request.GET["lugar"]
         find_home= Houses.objects.filter(lugar__icontains=lugar)
         return render(request,"result_search.html",{"respuesta":find_home, "lugar":lugar})
    else:
       
        respuesta= "no enviaste un dato valido"
        return render(request,"result_search.html",{"respuesta":respuesta})    
       
    
class SearchResultsView(ListView):
    model= Houses
    template_name="result_search2.html"
    
    def get_queryset(self):
        query= self.request.GET.get("q")
        object_list = Houses.objects.filter(Q(lugar__icontains=query)|Q(direccion__icontains=query)|Q(precio__icontains=query))
        return object_list
    
    
    
def about(request):   
    vendedores=Agentes.objects.all() 
    return render(request,'about.html',{"vendedores":vendedores})
        

class DeleteHouse(DeleteView):
    model=Houses
    success_url="/allprop"
    template_name="Houses_confirm_delete.html"
    
    
class Contactos_view(CreateView):
     model=Contacto
     form_class= ContactoForm
     template_name="contact.html"
     success_url = '/list'


def mesages_client(request):
    mesages=Contacto.objects.all()
    return render(request,"mesages.html",{"mensage":mesages})

def prueba6(request):
     mesages=Agentes.objects.all()
     houses=Houses.objects.all()
     return render(request,"prueba6.html",{"agent":mesages,"houses":houses})

#Funciones Usuarios
 
def loguin_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            user=authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "padre.html",{"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "padre.html",{"mensaje":"Datos incorrectos"})
        else:
            return render(request, "padre.html",{"mensaje":"Error en formulario"})  
    form= AuthenticationForm()
    return render(request, "login.html", {"form":form})

def register(request):
    if request.method == "POST":
        form= UserRegistroForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return render(request, "padre.html", {"mensaje":"Usuario Creado"})
    else:
        form=UserRegistroForm()
    
    return render(request, "registro.html",{"form":form})

class UserEditForma(UpdateView):
    
    form_class= EditRegistroForm
    template_name="edit_user.html"
    success_url = '/list'
    
    def get_object(self):
        return self.request.user 
    
class ChangePass(PasswordChangeView):
    
    form_class= PasswordCambioForm
    success_url = "edit_profile/"

#CALCULADORA    
def calculadora(request):
    return render(request, "calculadora.html")

def result(request):
    num1 = float(request.GET.get('number1'))
    num2 = float(request.GET.get('number2'))

    
    if request.GET.get('add') == "":
        ans = num1 + num2

    elif request.GET.get('subtract') == "":    
        ans = num1 - num2

    elif request.GET.get('multiply') == "":    
        ans = num1 * num2

    elif request.GET.get('potencia') == "":    
        ans = num1 ** num2    

    elif request.GET.get('pitagoras') == "":    
        ans =( (num1 * num1 ) + (num2 * num2)) ** 0.5 

    else:
        ans = num1 / num2

    return render(request, 'calculadora.html', {'ans': ans})



class AgentesLoad(CreateView):
     #model=Agentes
     form_class= AgentesForm
     #context = 'agente' 
     template_name="load_agent.html"
     success_url = '/'
     
     
def agentes_adm(request):
    agentes=Agentes.objects.all()
    return render(request,'agentes_adm.html', {"agentes":agentes})

class Agent_Upd(UpdateView):
    #form_class= AgentesForm
    model=Agentes
    fields="__all__"
    template_name="agent_update.html"
    success_url = '/'
    
class DeleteAgent(DeleteView):
    model=Agentes
    success_url="/"
    template_name="agent_del_conf.html"