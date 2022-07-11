from django.shortcuts import render

from rest_framework import generics 
from core.models import *
from .serializers import *

#create you views here.

class AlumnoViewSet(generics.ListAPIView):
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializers


class AlumnoFiltroViewSet(generics.ListAPIView):
	serializer_class = AlumnoSerializers	
	def get_queryset(self):
		nombre_alumno = self.kwargs['nombres_alumno']
		return Alumno.objects.filter(nombres_alumno=nombre_alumno)

class  AlumnoregistradoViewSet(generics.ListAPIView):
	serializer_class = AlumnoSerializers	
	def get_queryset(self):
		return Alumno.objects.filter(publicar=True)

class AlumnoPieViewSet(generics.ListAPIView):
	queryset = Alumnopie.objects.all()
	serializer_class = AlumnopieSerializers


class AlumnoPieFiltroViewSet(generics.ListAPIView):
	serializer_class = AlumnopieSerializers	
	def get_queryset(self):
		nombre_alumnopie = self.kwargs['nombre']
		return Alumnopie.objects.filter(nombre=nombre_alumnopie)

class  AlumnoPieregistradoViewSet(generics.ListAPIView):
	serializer_class = AlumnopieSerializers	
	def get_queryset(self):
		return Alumnopie.objects.filter(publicar=True)

class EscuelaViewSet(generics.ListAPIView):
	queryset = Escuela.objects.all()
	serializer_class = EscuelaSerializers


class EscuelaFiltroViewSet(generics.ListAPIView):
	serializer_class = EscuelaSerializers	
	def get_queryset(self):
		nombre = self.kwargs['nombre_escuela']
		return Escuela.objects.filter(nombre_escuela=nombre)

class  EscuelaregistradoViewSet(generics.ListAPIView):
	serializer_class = EscuelaSerializers	
	def get_queryset(self):
		return Escuela.objects.filter(publicar=True)


class CursoViewSet(generics.ListAPIView):
	queryset = Curso.objects.all()
	serializer_class = CursoSerializers


class CursoFiltroViewSet(generics.ListAPIView):
	serializer_class = CursoSerializers	
	def get_queryset(self):
		nombrecurso = self.kwargs['nomcurso']
		return Curso.objects.filter(nomcurso=nombrecurso)

class  CursoregistradoViewSet(generics.ListAPIView):
	serializer_class = CursoSerializers	
	def get_queryset(self):
		return Curso.objects.filter(publicar=True)


class ApoderadoViewSet(generics.ListAPIView):
	queryset = Apoderado.objects.all()
	serializer_class = ApoderadoSerializers