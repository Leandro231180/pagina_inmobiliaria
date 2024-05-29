from django import forms
from .models import Houses, Contacto, Agentes 
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User

class CreateNewSale(forms.ModelForm):
    class Meta:
        model= Houses
        fields = ("lugar","foto","foto2","foto3","direccion","precio","beds","baths","description", "Agente")
    widgets={
        "lugar": forms.TextInput(attrs={"class":"form-control"}),
        "foto": forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"})),
        "foto2": forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"})),
        "foto3": forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"})),
        "direccion": forms.NumberInput(attrs={"class":"form-control"}),
        "precio": forms.NumberInput(attrs={"class":"form-control"}),
        "beds": forms.NumberInput(attrs={"class":"form-control"}),
        "baths": forms.NumberInput(attrs={"class":"form-control"}),
        "description": forms.Textarea(attrs={"class":"form-control"}),
        "agente": forms.Select(attrs={"class":"form-control"}),
        
  
    }   
        


        
class ContactoForm(forms.ModelForm):  
    class Meta:
        model=Contacto
        #fields=("contact_nombre","correo", "mensaje")
        fields='__all__'
        widgets={ 
             "contact_nombre":forms.TextInput(),
           "correo":forms.TextInput(),
             "mensaje":forms.Textarea(),     
       }
        
      
    
class UserRegistroForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email= forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password1: forms.CharField(max_length=50,label='Constraseña', widget=forms.PasswordInput)
    password2: forms.CharField(max_length=50,label='Confirma Constraseña', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','password2','email']
        help_texts={k:"" for k in fields}                
    def __init__(self, *args, **kwargs):
        super(UserRegistroForm,self).__init__(*args, **kwargs)    
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            
            
class EditRegistroForm(UserChangeForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    #Estan desactivados para prevenir que cualquiera se haga super usuario.-
    # last_login=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    # is_superuser=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    # is_staff=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    # is_active=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    # date_joined=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','password','email') #,'last_login','is_superuser','is_staf','is_active','date_joined')
        
        
class PasswordCambioForm(PasswordChangeForm):
    
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", 'type': 'password'}))
    new_password1=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class":"form-control", 'type': 'password'}))
    new_password2=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class":"form-control", 'type': 'password'}))
    
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')
        

class AgentesForm(forms.ModelForm):
    
    class Meta:
        model=Agentes
        fields='__all__'
       
    