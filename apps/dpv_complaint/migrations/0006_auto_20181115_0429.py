# Generated by Django 2.1.2 on 2018-11-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_complaint', '0005_auto_20181115_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='accepted',
            name='answer',
            field=models.CharField(choices=[('Explicada Causa de no Solucion', 'ECNS'), ('Tramite', 'Tramite'), ('Pendiente de Solucion', 'PS'), ('Pendiente de Respuesta', 'PR'), ('Solucion o Resuelto', 'S')], default='S', max_length=100, verbose_name='Actual Respuesta de la queja'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Esperando Respuesta de Tecnico', 'Esperando Respuesta de Tecnico'), ('Pendiente', 'P'), ('Esperando Asignacion', 'Esperando Asignacion'), ('Esperando aceptacion del jefe', 'Esperando aceptacion del jefe')], default='Pendiente', max_length=15, verbose_name='Estado de la Queja'),
        ),
    ]
