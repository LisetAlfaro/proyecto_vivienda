# Generated by Django 2.1.2 on 2018-12-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servidor', models.CharField(max_length=100)),
                ('puerto', models.CharField(max_length=3)),
                ('usuario', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=50)),
                ('usa_tls', models.BooleanField(default=False)),
                ('usa_ssl', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Configuración de correo',
            },
        ),
        migrations.CreateModel(
            name='FilesUploaded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo_mime', models.CharField(max_length=50)),
                ('extencion', models.CharField(max_length=5)),
                ('archivo', models.FileField(upload_to='')),
                ('tamanno', models.DecimalField(decimal_places=4, max_digits=12)),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nombre', 'extencion'],
            },
        ),
    ]
