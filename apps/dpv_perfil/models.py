from django.db import models
from django.contrib.auth.models import User
from apps.dpv_persona.models import PersonaNatural
from apps.dpv_nomencladores.models import AreaTrabajo, CentroTrabajo


# Create your models here.
class Perfil(models.Model):
    datos_usuario = models.ForeignKey(User, verbose_name="Datos del usuario", related_name="perfil_usuario", on_delete=models.CASCADE)
    datos_personales = models.OneToOneField(PersonaNatural, verbose_name="Datos Personales", related_name="perfil_datos", on_delete=models.CASCADE)
    notificacion_email = models.BooleanField(default=True, verbose_name="Notificar por Email",
                                             help_text="Marque para recibir las notificaciones por correo electrónico")
    documentacion_email = models.BooleanField(default=True, verbose_name="Recibir Documentos por Email",
                                              help_text="Marque para recibir la documentación por correo electronico")
    avatar = models.ImageField()
    centro_trabajo = models.ForeignKey(CentroTrabajo, verbose_name="Unidad", related_name="perfil_trabajo", on_delete=models.SET_DEFAULT, default='')
    depto_trabajo = models.ForeignKey(AreaTrabajo, verbose_name="Departamento", related_name="perfil_area", on_delete=models.SET_DEFAULT, default='')

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"