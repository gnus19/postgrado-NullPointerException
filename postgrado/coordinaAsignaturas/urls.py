# -*- coding: utf-8 -*-


from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout


app_name = 'coordinaAsignaturas'
urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', views.home),
	url(r'^principal/$', views.principal, name='principal'),
	url(r'^ver/$', views.verAsignaturas, name='verAsignaturas'),
	url(r'^agregar/$', views.agregarAsignatura, name='agregarAsignatura'),
	url(r'^modificar/(?P<codAsig>.+)/$', views.modificarAsignatura, name='modificarAsignatura'),
	url(r'^eliminar/(?P<codAsig>[-\w]+)', views.eliminarAsignatura, name="eliminarAsignatura"),
	url(r'^detalles/(?P<codAsig>.+)/$', views.detallesAsignatura, name='detallesAsignatura'),
	url(r'^<int:oferta_id>/$', views.verOfertas, name='oferta')
	#url(r'^logout/$', login, {'template_name': 'coordinaAsignaturas/logout.html'}),
]