from django.urls import path
from onsale import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView 
from .views import ListaCasasGeek, ModPublication, DetailView,ProductDetailView, DeleteHouse, Contactos_view,UserEditForma,ChangePass, UserChangeForm,ListaCasasGeek2, AgentesLoad,Agent_Upd,DeleteAgent
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('',views.index,name="inicio" ),    
    #path('22',views.excelente ), #sepuede borrar
    #path('33', views.prueba, name="loco"),#se puede borrar
    path("allprop", views.allproperties, name="allprop"),
    
    #CRUD
    path("CV",login_required(ListaCasasGeek.as_view()),name="LoadProp"),
    path("LoadProperty",login_required(ListaCasasGeek2.as_view()),name="LoadProperty"),
    
    path("<pk>/update", ModPublication.as_view()),
    path("<pk>/delete/",login_required(DeleteHouse.as_view())),
    path("prop/<int:pk>/",ProductDetailView.as_view(), name="detalle_casa"),
    path("padre",views.padre),
    path("hija", views.hija),
    path("LoadAgent",AgentesLoad.as_view(),name="LoadAgent"),
    path("<pk>/delete_agent/",login_required(DeleteAgent.as_view())),
    path("<pk>/agentUdt", Agent_Upd.as_view()),
    #path("list", views.listaprop, name="list_sales"),#sepuede borrar
    path("agent_adm", views.agentes_adm, name="agentes_list"),
   
    
    
    path("resultadob", views.search, name="buscador"),
    path("busca", views.busqueda_Prop, name="busca"),
    path("about", views.about, name="about"),
    path("contact",Contactos_view.as_view(), name="contact"),
    path("mensaje", views.mesages_client,name="mensaje"),
    
    
    # Usuario y Perfiles
    path("login", views.loguin_request, name="login"),
    path("registro", views.register, name="registro"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("edit_profile/", UserEditForma.as_view(template_name="edit_user.html"), name="edituser"),
    
    #path("password/", auth_views.PasswordChangeView.as_view(template_name='change_password.html')),
    path("password/", ChangePass.as_view(template_name='change_password.html')),
    
    #calculator
    path("calculadora", views.calculadora, name="calculadora"),
    path('result/', views.result, name='result'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
