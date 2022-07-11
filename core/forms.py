from tkinter import Widget
from tokenize import group
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User,Permission, Group


class EscuelaForm(forms.ModelForm):
    
    class Meta:
        model = Escuela
        fields = 'nombre_escuela', 'descripcion','municipio','imagen'
        

class ApoderadoForm(forms.ModelForm):
    
    class Meta:
        model = Apoderado
        fields = '__all__'
        
        
class AlumnoForm(forms.ModelForm):
    
    class Meta:
        model = Alumno
        fields = '__all__'

    #def __init__(self, escuela_id, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['curso'].queryset=Curso.objects.filter(escuela = escuela_id)
        
class AlumnoPieForm(forms.ModelForm):
    
    class Meta:
        model = Alumnopie
        fields = '__all__'

        widgets ={
            "fecha_ingreso": forms.SelectDateWidget()
        }

                

class PfsForm(forms.ModelForm):
    
    class Meta:
        model = Pfs
        fields = '__all__'


class ComunaForm(forms.ModelForm):
    
    class Meta:
        model = Comuna
        fields = '__all__'


class MuniForm(forms.ModelForm):
    
    class Meta:
        model = Municipio
        fields = '__all__'

class cupoForm(forms.ModelForm):
    
    class Meta:
        model = Cupoextra
        fields = '__all__'

        widgets ={
            "fecha_solicitud": forms.SelectDateWidget()
        }


class evaluacionForm(forms.ModelForm):
    
    class Meta:
        model = Evaluacion
        fields = '__all__'



class CupoForm(forms.ModelForm):

    
    class Meta:
        model = Cupoextra
        fields = '__all__'


class cursoForm(forms.ModelForm):

    
    class Meta:
        model = Curso
        fields = '__all__'



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email', 'groups', 'password1', 'password2' ]
#