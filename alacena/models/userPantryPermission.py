from django.db import models
from authApp.models.user import User
from alacena.models.pantry import Pantry

class PantryProfile(models.TextChoices):
    FAMILIA = 'F', ('Familia')
    INVITADO = 'I', ('Invitado')

class UserPantryPermission(models.Model):

    creation_date = models.DateTimeField('Fecha de adicion', auto_now_add= True)
    last_modification_date = models.DateTimeField('Fecha ultima modificacion', auto_now= True)
    user = models.ForeignKey(User, verbose_name='Usuario',on_delete=models.CASCADE)
    profile = models.CharField('Perfil', choices=PantryProfile.choices, max_length= 1, default= PantryProfile.INVITADO)
    active = models.BooleanField('Activo', default= True)
    pantry = models.ForeignKey(Pantry, verbose_name='Alacena', on_delete= models.CASCADE)