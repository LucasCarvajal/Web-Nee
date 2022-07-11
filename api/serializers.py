from rest_framework import serializers
from core.models import * 


class AlumnoSerializers(serializers.ModelSerializer):
	class Meta:
		model = Alumno
		fields = ["id_alumno","nombres_alumno","apellidos_alumno","edad","curso","apoderado"]


class AlumnopieSerializers(serializers.ModelSerializer):
	class Meta:
		model = Alumnopie
		fields = ["id_alumnopie","alumno","fecha_ingreso","evaluacion","curso","justificativo_ingreso"]


class EscuelaSerializers(serializers.ModelSerializer):
	class Meta:
		model = Escuela
		fields = ["id_escuela","nombre_escuela","descripcion","municipio","imagen"]

  
class CursoSerializers(serializers.ModelSerializer):
	class Meta:
		model = Curso
		fields = ["id_curso","nomcurso","escuela","cupos","cupos_pie"]

class ApoderadoSerializers(serializers.ModelSerializer):
	class Meta:
		model = Apoderado
		fields = ["id_apoderado","nombre_apoderado","apellido_apoderado","celular","correo"]


   
