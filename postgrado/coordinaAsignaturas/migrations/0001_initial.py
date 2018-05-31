# Generated by Django 2.0.4 on 2018-05-31 21:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('codAsig', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('codDpto', models.CharField(choices=[('EA', 'Estudios Ambientales'), ('CE', 'Ciencias Económicas y Administrativas'), ('CC', 'Ciencia y Tecnología del Comportamiento'), ('FIS', 'Física'), ('QM', 'Química'), ('MC', 'Mecánica'), ('MA', 'Matemáticas Puras y Aplicadas'), ('CI', 'Computación y Ciencias de la Información'), ('CO', 'Cómputo Científico y Estadística'), ('EC', 'Electrónica y Circuitos'), ('TF', 'Termodinámica y Fenómenos de Transferencia'), ('PS', 'Procesos y Sistemas'), ('MT', 'Ciencias de los Materiales'), ('GC', 'Ciencias de la Tierra'), ('LL', 'Lengua y Literatura'), ('ID', 'Idiomas'), ('FLX', 'Filosofía'), ('CS', 'Ciencias Sociales'), ('DA', 'Diseño Arquitectura y Artes Plásticas'), ('PL', 'Planificación Urbana'), ('BC', 'Biología Celular'), ('EA', 'Estudios Ambientales'), ('BO', 'Biología de Organismos'), ('PB', 'Tecnología de Procesos Biológicos y Bioquímicos')], max_length=6)),
                ('creditos', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)])),
                ('nomAsig', models.CharField(max_length=80)),
                ('progAsig', models.CharField(max_length=20)),
                ('diaHora', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ('nomAsig',),
            },
        ),
        migrations.CreateModel(
            name='Coordinacion',
            fields=[
                ('nomCoord', models.CharField(choices=[('MAT', 'Matemáticas'), ('CB', 'Ciencias Biológicas'), ('CI', 'Ciencias de la Computación'), ('CAN', 'Ciencias de los Alimentos y Nutrición'), ('FIS', 'Física'), ('QM', 'Química'), ('DIC', 'Doctorado Interdisciplinario en Ciencias'), ('CP', 'Ciencia Política'), ('DYA', 'Desarrollo y Ambiente'), ('EDU', 'Educación'), ('EH', 'Estudios Humanos'), ('FLX', 'Filosofía'), ('EGE', 'Estudios en Gerencia y Economía'), ('LA', 'Lingüística Aplicada'), ('LIT', 'Literatura'), ('MUS', 'Música'), ('PSI', 'Psicología'), ('EXT', 'Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional'), ('DEI', 'Doctorado en Ingeniería'), ('ECO', 'Estadística Computacional'), ('IE', 'Ingeniería Electrónica'), ('IT', 'Ingeniería y Tecnología Eléctrica'), ('GC', 'Ingeniería Geofísica'), ('IM', 'Ingeniería Mecánica/Civil'), ('IQ', 'Ingeniería Química'), ('MTR', 'Ingeniería de Materiales'), ('IS', 'Ingeniería de Sistemas'), ('ITB', 'Ingeniería de Telecomunicaciones/Biomédica'), ('P-CBA', 'Postgrado - Ciencias Básicas y Aplicadas'), ('P-CSH', 'Postgrado - Ciencias Sociales y Humanidades'), ('P-IT', 'Postgrado - Ingeniería y Tecnología')], max_length=4, primary_key=True, serialize=False)),
                ('asignaturas', models.ManyToManyField(to='coordinaAsignaturas.Asignatura')),
            ],
            options={
                'verbose_name_plural': 'Coordinaciones',
            },
        ),
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nomCoord', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coordinaAsignaturas.Coordinacion')),
            ],
            options={
                'verbose_name_plural': 'Coordinadores',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('carnet', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(validators=[django.core.validators.MinValueValidator(2018), django.core.validators.MaxValueValidator(2050)])),
                ('trimestre', models.CharField(choices=[('E-M', 'Enero-Marzo'), ('A-J', 'Abril-Julio'), ('S-D', 'Septiembre-Diciembre')], max_length=7)),
                ('asignaturas', models.ManyToManyField(to='coordinaAsignaturas.Asignatura')),
            ],
            options={
                'verbose_name_plural': 'Inscripciones',
            },
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trimestre', models.CharField(choices=[('E-M', 'Enero-Marzo'), ('A-J', 'Abril-Julio'), ('S-D', 'Septiembre-Diciembre')], max_length=7)),
                ('anio', models.IntegerField(validators=[django.core.validators.MinValueValidator(2018), django.core.validators.MaxValueValidator(2050)])),
                ('asignaturas', models.ManyToManyField(to='coordinaAsignaturas.Asignatura')),
                ('nomCoord', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coordinaAsignaturas.Coordinacion')),
            ],
            options={
                'ordering': ('anio',),
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('ciProf', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999999)])),
                ('nomProf', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.AddField(
            model_name='estudiante',
            name='inscripciones',
            field=models.ManyToManyField(to='coordinaAsignaturas.Inscripcion'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='coordinaAsignaturas.Profesor'),
        ),
    ]
