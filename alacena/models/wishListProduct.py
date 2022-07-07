from django.db import models
from authApp.models.user import User
from .pantry import Pantry
from .productPantry import Unit

class WishListProduct(models.Model):

    name = models.CharField('Nombre producto', max_length=50)
    pantry = models.ForeignKey(Pantry, verbose_name='Alacena', on_delete= models.CASCADE, null= True)
    added_by = models.ForeignKey(User, verbose_name='Añadido por', on_delete= models.CASCADE, null= True)
    added_date = models.DateTimeField('Añadido', auto_now_add= True)
    quantity = models.IntegerField('Cantidad', default= 1)
    unit = models.CharField('Unidad', choices= Unit.choices, default= Unit.U, max_length= 20)
    active = models.BooleanField('Activo', default= True)