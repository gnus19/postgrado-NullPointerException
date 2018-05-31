# -*- coding: utf-8 -*-

'''
Universidad Simón Bolívar (USB)
Ingeniería de Software I - CI3715
Equipo Null Pointer Exception
Modelos para la aplicación coordinaAsignaturas

Ver modelo UML e informe técnico para mayor información

'''

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

fecha = datetime.datetime.now()

# Departamentos de la USB
# junto a sus abreviaciones

DPTOS = (
    ('EA','Estudios Ambientales'),
    ('CE','Ciencias Económicas y Administrativas'),
    ('CC','Ciencia y Tecnología del Comportamiento'),
    ('FIS','Física'),
    ('QM','Química'),
    ('MC','Mecánica'),
    ('MA','Matemáticas Puras y Aplicadas'),
    ('CI','Computación y Ciencias de la Información'),
    ('CO','Cómputo Científico y Estadística'),
    ('EC','Electrónica y Circuitos'),
    ('TF','Termodinámica y Fenómenos de Transferencia'),
    ('PS','Procesos y Sistemas'),
    ('MT','Ciencias de los Materiales'),
    ('GC','Ciencias de la Tierra'),
    ('LL','Lengua y Literatura'),
    ('ID','Idiomas'),
    ('FLX','Filosofía'),
    ('CS','Ciencias Sociales'),
    ('DA','Diseño Arquitectura y Artes Plásticas'),
    ('PL','Planificación Urbana'),
    ('BC','Biología Celular'),
    ('EA','Estudios Ambientales'),
    ('BO','Biología de Organismos'),
    ('PB','Tecnología de Procesos Biológicos y Bioquímicos'),
    )

# Coordinaciones de postgrado de la USB
# junto a sus abreviaciones

COORDS = (
    ('MAT','Matemáticas'),
    ('CB','Ciencias Biológicas'),
    ('CI','Ciencias de la Computación'),
    ('CAN','Ciencias de los Alimentos y Nutrición'),
    ('FIS','Física'),
    ('QM','Química'),
    ('DIC','Doctorado Interdisciplinario en Ciencias'),
    ('CP', 'Ciencia Política'),
    ('DYA', 'Desarrollo y Ambiente'),
    ('EDU', 'Educación'),
    ('EH', 'Estudios Humanos'),
    ('FLX', 'Filosofía'),
    ('EGE','Estudios en Gerencia y Economía'),
    ('LA','Lingüística Aplicada'),
    ('LIT','Literatura'),
    ('MUS','Música'),
    ('PSI','Psicología'),
    ('EXT','Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional'),
    ('DEI','Doctorado en Ingeniería'),
    ('ECO','Estadística Computacional'),
    ('IE','Ingeniería Electrónica'),
    ('IT','Ingeniería y Tecnología Eléctrica'),
    ('GC','Ingeniería Geofísica'),
    ('IM','Ingeniería Mecánica/Civil'),
    ('IQ','Ingeniería Química'),
    ('MTR','Ingeniería de Materiales'),
    ('IS','Ingeniería de Sistemas'),
    ('ITB','Ingeniería de Telecomunicaciones/Biomédica'),
    ('P-CBA','Postgrado - Ciencias Básicas y Aplicadas'),
    ('P-CSH','Postgrado - Ciencias Sociales y Humanidades'),
    ('P-IT','Postgrado - Ingeniería y Tecnología'),
    )

# Los tres períodos trimestrales estándar de la USB

TRIMESTRES   = (('E-M','Enero-Marzo'),('A-J','Abril-Julio'),('S-D','Septiembre-Diciembre'))
    
# Las clases descritas a continuación siguen el orden de dependencia igual al que
# poseen actualmente. Modificar con cuidado

# Profesor de la USB
class Profesor(models.Model):
    ciProf      = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(99999999)], primary_key=True)
    nomProf     = models.CharField(max_length=80)

    def __str__(self):
        return self.nomProf

    class Meta:
        verbose_name_plural = "Profesores"

# Asignatura de postgrado
# El campo diaHora recibe restricciones de formato (e.g. "Lunes 7-8, Martes 5-6")
# a través de la interfaz gráfica.
class Asignatura(models.Model):
    codAsig     = models.CharField(max_length=7, primary_key=True)
    codDpto     = models.CharField(max_length=6, choices = DPTOS)
    creditos    = models.IntegerField(choices = ((0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),
                                                (7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15)))
    nomAsig     = models.CharField(max_length=80)
    progAsig    = models.CharField(max_length=20)
    diaHora     = models.CharField(max_length=60)
    prof        = models.ForeignKey(Profesor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nomAsig

    class Meta:
        ordering = ('nomAsig',)

# Coordinación de postgrado
# Puede tener muchas asignaturas asociadas sin importar el departamento.
class Coordinacion(models.Model):
    nomCoord    = models.CharField(max_length=4, choices = COORDS, primary_key=True)
    asignaturas = models.ManyToManyField(Asignatura)

    def __str__(self):
        return self.nomCoord

    class Meta:
        verbose_name_plural = "Coordinaciones"

# Coordinador de coordinación de postgrado
# Tiene un usuario Django asociado con permisología específica
class Coordinador(models.Model):
    nomCoord    = models.ForeignKey(Coordinacion, on_delete=models.PROTECT)
    usuario     = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name_plural = "Coordinadores"

# Oferta de asignaturas proveniente de una coordinación de postgrado
# Puede tener muchas asignaturas. Es una oferta con trimestre y año.
class Oferta(models.Model):
    nomCoord    = models.ForeignKey(Coordinacion, on_delete=models.PROTECT)
    trimestre   = models.CharField(max_length=7, choices = TRIMESTRES)
    asignaturas = models.ManyToManyField(Asignatura)
    anio        = models.IntegerField(validators=[MinValueValidator(fecha.year),MaxValueValidator(2050)])

    def __str__(self):
        return (str(self.trimestre)+" "+str(self.anio))

    class Meta:
        ordering = ('anio',)

# Inscripción de un estudiante
# Consta de asignaturas, año y trimestre.
# Se puede calcular la suma de créditos (carga académica)
# con sumCreditos()
class Inscripcion(models.Model):
    asignaturas = models.ManyToManyField(Asignatura)
    anio        = models.IntegerField(validators=[MinValueValidator(fecha.year),MaxValueValidator(2050)])
    trimestre   = models.CharField(max_length=7, choices=TRIMESTRES)

    def __str__(self):
        return (self.trimestre+", "+str(self.anio))

    def sumCreditos(self):
        suma = 0
        for a in self.asignaturas:
            suma += a.creditos
        return (suma)

    class Meta:
        verbose_name_plural = "Inscripciones"

# Estudiante de postgrado
# Está asociado a un usuario Django
# Necesita tener alguna inscripción para contar como estudiante.
class Estudiante(models.Model):
    usuario         = models.OneToOneField(User, on_delete=models.CASCADE)
    carnet          = models.CharField(max_length=12, primary_key=True)
    inscripciones   = models.ManyToManyField(Inscripcion)