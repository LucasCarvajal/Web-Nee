# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#{% for i in Escuela %}
#<select name="nombre_escuela" id={{i}}>
#   <option value="" selected="selected">Selecciona una escuela</option>
#    <option value={{i}}>Escuela.nombre_escuela</option>
#</select>
#{% endfor %}


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombres_alumno = models.CharField(max_length=100)
    apellidos_alumno = models.CharField(max_length=100)
    edad = models.FloatField()
    curso = models.ForeignKey('Curso', models.DO_NOTHING)
    apoderado = models.ForeignKey('Apoderado', models.DO_NOTHING)


    def __str__(self):
        return self.nombres_alumno

    class Meta:
        managed = False
        db_table = 'alumno'

    


class Alumnopie(models.Model):
    id_alumnopie = models.AutoField(primary_key=True)
    justificativo_ingreso = models.CharField(max_length=500)
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    fecha_ingreso = models.DateField()
    evaluacion = models.ForeignKey('Evaluacion', models.DO_NOTHING)
    curso = models.ForeignKey('Curso', models.DO_NOTHING)

    def __int__(self):
        return self.alumno

    class Meta:
        managed = False
        db_table = 'alumnopie'


class Apoderado(models.Model):
    id_apoderado = models.AutoField(primary_key=True)
    nombre_apoderado = models.CharField(max_length=50)
    apellido_apoderado = models.CharField(max_length=50)
    celular = models.IntegerField()
    correo = models.EmailField(max_length=50)
   

    def __str__(self):
        return self.nombre_apoderado

    class Meta:
        managed = False
        db_table = 'apoderado'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_comuna

    class Meta:
        managed = False
        db_table = 'comuna'


class Cupoextra(models.Model):
    id_cupoextra = models.AutoField(primary_key=True)
    fecha_solicitud = models.DateField()
    justificacion_cupo = models.CharField(max_length=200)
    documento = models.FileField(upload_to="archivos")
    escuela = models.ForeignKey('Escuela', models.DO_NOTHING)

    def __int__(self):
        return self.escuela

    class Meta:
        managed = False
        db_table = 'cupoextra'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nomcurso = models.CharField(max_length=20)
    escuela = models.ForeignKey('Escuela', models.DO_NOTHING)
    cupos = models.IntegerField()
    cupos_pie = models.IntegerField()

    def __str__(self):
        return self.nomcurso
    class Meta:
        managed = False
        db_table = 'curso'


class Escuela(models.Model):
    id_escuela = models.AutoField(primary_key=True)
    nombre_escuela = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    municipio = models.ForeignKey('Municipio', models.DO_NOTHING)
    imagen = models.ImageField(upload_to="logo", null=True)
    

    def __str__(self):
        return self.nombre_escuela

    class Meta:
        managed = False
        db_table = 'escuela'


class Evaluacion(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    archivos_diagnostico = models.FileField(upload_to="Diagnostico")
    evaluacion_especialista = models.CharField(max_length=500)



    class Meta:
        managed = False
        db_table = 'evaluacion'


class Municipio(models.Model):
    id_muni = models.AutoField(primary_key=True)
    nombre_muni = models.CharField(max_length=10)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING)

    def __str__(self):
        return self.nombre_muni

    class Meta:
        managed = False
        db_table = 'municipio'


class Pfs(models.Model):
    id_pfs = models.AutoField(primary_key=True)
    psicopedagogia = models.BooleanField()
    terapeutaocupacional = models.BooleanField()
    pediatra = models.BooleanField()
    fonoaudiologa = models.BooleanField()
    ed_diferencial = models.BooleanField()
    escuela = models.ForeignKey(Escuela, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pfs'
