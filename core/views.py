from ast import Return
from dataclasses import dataclass
from email import message
from re import A
from tokenize import group
from urllib import request
from django.contrib.auth.models import User,Permission, Group
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required 
from django.contrib.contenttypes.models import ContentType 
from django.db.models import Count  , Q
# Create your views here.
def home(request):



    return render(request, 'core/home.html')

@permission_required('core.view_escuela')
def listarEstablecimiento(request):
    escuela = Escuela.objects.all()
    data = {
        'escuela': escuela
    }
    return render(request, 'core/Listar/listarEstablecimiento.html', data)

@permission_required('core.view_alumno')
def listarAlumno(request):
    alumno = Alumno.objects.all()
    data = {
        'alumno': alumno
    }
    return render(request, 'core/Listar/listarAlumno.html', data)

@permission_required('core.add_escuela')
def formularioescuela(request):

    data = {
        'formulario': EscuelaForm()
    }
    
    if request.method == 'POST':
        formulario = EscuelaForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
            return redirect(to="listarEstablecimiento")
        else:
            data["formulario"] = formulario
        
    return render(request, 'core/Agregar/formularioescuela.html', data)


@permission_required('core.add_alumno')
def formularioalumno(request):
    data = {
        'formalu': AlumnoForm()
    }

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
            return redirect(to="listarAlumno")
        else:
            data["formalu"] = formulario
    
 
    return render(request, 'core/Agregar/formularioalumno.html',data)

    

@permission_required('core.add_apoderado')
def formularioapoderado(request):
    data = {
        'formapo': ApoderadoForm()
    }
    if request.method == 'POST':
        formulario = ApoderadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
            return redirect(to="listarapoderado")
        else:
            data["formapo"] = formulario
    return render(request, 'core/Agregar/formularioapoderado.html',data)
 
  
@permission_required('core.add_alumnopie')    
def formularioalumnopie(request):


    data = {
        'formupie': AlumnoPieForm(data=request.POST,files=request.FILES)
    }


    if request.method == 'POST':
        formulario = AlumnoPieForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
            return redirect(to="listaralumnopie")
        else:
            data["formupie"] = formulario
    return render(request, 'core/Agregar/formularioalumnopie.html', data)

@permission_required('core.add_pfs')
def formularioespecialista(request):
    data = {
        'formpfs': PfsForm()
    }
    if request.method == 'POST':
        formulario = PfsForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
        else:
            data["formpfs"] = formulario

    return render(request, 'core/Agregar/formularioespecialista.html', data)


@permission_required('core.add_comuna')
def agregarcomuna(request):
    data = {
        'forcom': ComunaForm()
    }
    if request.method == 'POST':
        formulario = ComunaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
            return redirect(to="listarcomuna")
        else:
            data["forcom"] = formulario
    return render(request, 'core/Agregar/agregarcomuna.html', data)

@permission_required('core.add_municipio')
def agregarmuni(request):
    data = {
        'formuni': MuniForm()
    }
    if request.method == 'POST':
        formulario = MuniForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
            return redirect(to="listarmuni")
        else:
            data["formuni"] = formulario
    return render(request, 'core/Agregar/agregarmuni.html', data)

@permission_required('core.add_cupoextra')
def agregarcupo(request):
    data = {
        'forcupo': cupoForm()
    }
    if request.method == 'POST':
        formulario = cupoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
            return redirect(to="listarcupo")

        else:
            data["forcupo"] = formulario
    return render(request, 'core/Agregar/agregarcupoextra.html', data)

@permission_required('core.add_curso')
def agregarcurso(request):

    data = {
        'forcur': cursoForm()
    }
    if request.method == 'POST':
        formulario = cursoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
            return redirect(to="listarcurso")

        else:
            data["forcur"] = formulario
    return render(request, 'core/Agregar/agregarcurso.html', data)

@permission_required('core.add_evaluacion')
def agregarevaluacion(request):
    data = {
        'foreva': evaluacionForm()
    }
    if request.method == 'POST':
        formulario = evaluacionForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
            return redirect(to="listarevaluacion")
        else:
            data["foreva"] = formulario
    return render(request, 'core/Agregar/agregarevaluacion.html', data)

@permission_required('core.view_pfs')
def listarespecialista(request):
    pfs = Pfs.objects.all()
    data = {
        'pfs': pfs
    }
    return render(request, 'core/Listar/listarEspecialista.html', data)

@permission_required('core.view_alumnopie')
def listaralumnopie(request):
    alumnopie = Alumnopie.objects.all()
    data = {
        'alumnopie': alumnopie
    }
    return render(request, 'core/Listar/listarAlumnoPie.html', data)

@permission_required('core.view_curso')
def listarcurso(request):
    curso = Curso.objects.all()
    data = {
        'curso': curso
    }
    return render(request, 'core/Listar/listarCurso.html', data)

@permission_required('core.view_comuna')
def listarcomuna(request):
    comuna = Comuna.objects.all()
    data = {
        'comuna': comuna
    }
    return render(request, 'core/Listar/listarComuna.html', data)    

@permission_required('core.view_apoderado')
def listarapoderado(request):
    apoderado = Apoderado.objects.all()
    data = {
        'apoderado': apoderado
    }
    return render(request, 'core/Listar/listarApoderado.html', data)


@permission_required('core.view_evaluacion')
def listarevaluacion(request):
    evaluacion = Evaluacion.objects.all()
    data = {
        'evaluacion': evaluacion
    }
    return render(request, 'core/Listar/listarEvaluacion.html', data)

@permission_required('core.change_alumno')
def modificar_Alumno(request, id_alumno):
    
    alumno = get_object_or_404(Alumno, id_alumno=id_alumno)

    data ={
        'formalu': AlumnoForm(instance=alumno)
    }
    if request.method == 'POST':
        formulario = AlumnoForm(data=request.POST, instance=alumno, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarAlumno")
        else:
            data["formalu"] = formulario

    return render(request, 'core/Modificar/modificarAlumno.html', data)

@permission_required('core.change_comuna')
def modificar_Comuna(request, id_comuna):
    
    comuna = get_object_or_404(Comuna, id_comuna=id_comuna)

    data ={
        'forcom': ComunaForm(instance=comuna)
    }
    if request.method == 'POST':
        formulario = ComunaForm(data=request.POST, instance=comuna, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarcomuna")
        else:
            data["forcom"] = formulario

    return render(request, 'core/Modificar/modificarComuna.html', data)

@permission_required('core.delete_apoderado')
def eliminar_Comuna(request, id_comuna):
    comuna = get_object_or_404(Comuna, id_comuna=id_comuna)
    comuna.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarcomuna")


@permission_required('core.delete_alumno')
def eliminar_Alumno(request, id_alumno):
    alumno = get_object_or_404(Alumno, id_alumno=id_alumno)
    alumno.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarAlumno")

@permission_required('core.change_alumnopie')
def modificar_AlumnoPie(request, id_alumnopie):
    
    alumnopie = get_object_or_404(Alumnopie, id_alumnopie=id_alumnopie)

    data ={
        'formupie': AlumnoPieForm(instance=alumnopie)
    }
    if request.method == 'POST':
        formulario = AlumnoPieForm(data=request.POST, instance=alumnopie, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listaralumnopie")
        else:
            data["formupie"] = formulario

    return render(request, 'core/Modificar/modificarAlumnoPie.html', data)

@permission_required('core.delete_alumnopie')
def eliminar_AlumnoPie(request, id_alumnopie):
    alumnopie = get_object_or_404(Alumnopie, id_alumnopie=id_alumnopie)
    alumnopie.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listaralumnopie")

@permission_required('core.change_apoderado')
def modificar_Apoderado(request, id_apoderado):
    
    apoderado = get_object_or_404(Apoderado, id_apoderado=id_apoderado)

    data ={
        'formapo': ApoderadoForm(instance=apoderado)
    }
    if request.method == 'POST':
        formulario = ApoderadoForm(data=request.POST, instance=apoderado, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarapoderado")
        else:
            data["formapo"] = formulario

    return render(request, 'core/Modificar/modificarApoderado.html', data)

@permission_required('core.delete_apoderado')
def eliminar_Apoderado(request, id_apoderado):
    apoderado = get_object_or_404(Apoderado, id_apoderado=id_apoderado)
    apoderado.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarapoderado")

@permission_required('core.change_curso')
def modificar_Curso(request, id_curso):
    
    curso = get_object_or_404(Curso, id_curso=id_curso)

    data ={
        'forcur': cursoForm(instance=curso)
    }
    if request.method == 'POST':
        formulario = cursoForm(data=request.POST, instance=curso, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarcurso")
        else:
            data["forcur"] = formulario

    return render(request, 'core/Modificar/modificarCurso.html', data)

@permission_required('core.delete_curso')
def eliminar_Curso(request, id_curso):
    curso = get_object_or_404(Curso, id_curso=id_curso)
    curso.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarcurso")

@permission_required('core.change_pfs')
def modificar_Pfs(request, id_pfs):
    
    pfs = get_object_or_404(Pfs, id_pfs=id_pfs)

    data ={
        'formpfs': PfsForm(instance=pfs)
    }
    if request.method == 'POST':
        formulario = PfsForm(data=request.POST, instance=pfs, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarespecialista")
        else:
            data["formpfs"] = formulario

    return render(request, 'core/Modificar/modificarEspecialista.html', data)

@permission_required('core.delete_pfs')
def eliminar_Pfs(request, id_pfs):
    pfs = get_object_or_404(Pfs, id_pfs=id_pfs)
    pfs.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarespecialista")

@permission_required('core.change_escuela')
def modificar_Establecimiento(request, id_escuela):
    
    escuela = get_object_or_404(Escuela, id_escuela=id_escuela)

    data ={
        'formulario': EscuelaForm(instance=escuela)
    }
    if request.method == 'POST':
        formulario = EscuelaForm(data=request.POST, instance=escuela, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarEstablecimiento")
        else:
            data["formulario"] = formulario

    return render(request, 'core/Modificar/modificarEstablecimiento.html', data)

@permission_required('core.delete_escuela')
def eliminar_Establecimiento(request, id_escuela):
    escuela = get_object_or_404(Escuela, id_escuela=id_escuela)
    escuela.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarEstablecimiento")

@permission_required('core.change_evaluacion')
def modificar_Evaluacion(request, id_diagnostico):
    
    evaluacion = get_object_or_404(Evaluacion, id_diagnostico=id_diagnostico)

    data ={
        'foreva': evaluacionForm(instance=evaluacion)
    }
    if request.method == 'POST':
        formulario = evaluacionForm(data=request.POST, instance=evaluacion, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarevaluacion")
        else:
            data["foreva"] = formulario

    return render(request, 'core/Modificar/modificarEvaluacion.html', data)

@permission_required('core.delete_evaluacion')
def eliminar_Evaluacion(request, id_diagnostico):
    evaluacion = get_object_or_404(Evaluacion, id_diagnostico=id_diagnostico)
    evaluacion.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarevaluacion")

@permission_required('core.view_municipio')
def listarmuni(request):
    muni = Municipio.objects.all()
    data = {
        'muni': muni
    }
    return render(request, 'core/Listar/listarmunicipio.html', data)

@permission_required('core.change_municipio')
def modificar_Muni(request, id_muni):
    
    muni = get_object_or_404(Municipio, id_muni=id_muni)

    data ={
        'formuni': MuniForm(instance=muni)
    }
    if request.method == 'POST':
        formulario = MuniForm(data=request.POST, instance=muni, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarmuni")
        else:
            data["formuni"] = formulario

    return render(request, 'core/Modificar/modificarMuni.html', data)

@permission_required('core.delete_municipio')
def eliminar_Muni(request, id_muni):
    muni = get_object_or_404(Municipio, id_muni=id_muni)
    muni.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarmuni")

def registro(request):
    data = {
        'formres': CustomUserCreationForm 
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Guardado Correctamente")
        else:
            data["formres"] = formulario
    return render(request, 'registration/registro.html', data )

@permission_required('core.change_cupoextra')
def modificar_cupo(request, id_cupoextra):
    
    cupo = get_object_or_404(Cupoextra, id_cupoextra=id_cupoextra)

    data ={
        'forcupo': cupoForm(instance=cupo)
    }
    if request.method == 'POST':
        formulario = cupoForm(data=request.POST, instance=cupo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listarcupo")
        else:
            data["forcupo"] = formulario

    return render(request, 'core/Modificar/modificarCupo.html', data)

@permission_required('core.delete_cupoextra')
def eliminar_Cupo(request, id_cupoextra):
    cupo = get_object_or_404(Cupoextra, id_cupoextra=id_cupoextra)
    cupo.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listarcupo")

@permission_required('core.view_cupoextra')
def listarcupo(request):
    cupo = Cupoextra.objects.all()
    data = {
        'cupo': cupo
    }
    return render(request, 'core/Listar/listarcupo.html', data)

#Alumnopie.objects.filter(="el valor que buscas").annotate(total=Count('nombre'))

def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        ' {body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    ) 

