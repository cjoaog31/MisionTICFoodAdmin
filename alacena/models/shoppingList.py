from django.db import models
from authApp.models.user import User

class ShoppingList(models.Model):

    created_by = models.ForeignKey(User,verbose_name='Creado por', on_delete= models.CASCADE, null= True)
    creation_date = models.DateTimeField('Fecha de creacion', auto_now_add= True)
    active = models.BooleanField('activa', default= True)