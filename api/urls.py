from django.urls import re_path
from rest_framework import urlpatterns, views
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns=[
    re_path(r'^api/alumno/$',views.AlumnoViewSet.as_view()),
    re_path(r'^api/alumno_nombre/(?P<nombres_alumno>.+)$',views.AlumnoFiltroViewSet.as_view()),
	re_path(r'^api/Alumno_publicada/$',views.AlumnoregistradoViewSet.as_view()),
    re_path(r'^api/alumnopie/$',views.AlumnoPieViewSet.as_view()),
    re_path(r'^api/alumnopie_nombre/(?P<hola>.+)$',views.AlumnoPieFiltroViewSet.as_view()),
    re_path(r'^api/alumnopie_publicada/$',views.AlumnoPieregistradoViewSet.as_view()),
    re_path(r'^api/curso/$',views.CursoViewSet.as_view()),
    re_path(r'^api/curso_nombre/(?P<nomcurso>.+)$',views.CursoFiltroViewSet.as_view()),
    re_path(r'^api/curso_publicada/$',views.CursoregistradoViewSet.as_view()),
    re_path(r'^api/escuela/$',views.EscuelaViewSet.as_view()),
    re_path(r'^api/escuela_nombre/(?P<nombre_escuela>.+)$',views.EscuelaFiltroViewSet.as_view()),
    re_path(r'^api/escuela_publicada/$',views.EscuelaregistradoViewSet.as_view()),
    re_path(r'^api/apoderado/$',views.ApoderadoViewSet.as_view()),
]
	
