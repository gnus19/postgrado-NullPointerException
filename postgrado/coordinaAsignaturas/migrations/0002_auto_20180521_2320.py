# Generated by Django 2.0.4 on 2018-05-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinaAsignaturas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='anio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='ciProf',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]