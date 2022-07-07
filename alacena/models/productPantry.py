from django.db import models
from authApp.models.user import User
from .product import Product
from .pantry import Pantry


class Unit(models.TextChoices):
    KG = 'KG', ('Kilogramo')
    LB = 'LB', ('Libra')
    G = 'G', ('Gramo')
    U = 'U', ('Unidad')
    L = 'L', ('Litro')
    ML = 'ML', ('Mililitro')


class ProductPantry(models.Model):

    product = models.ForeignKey(Product, verbose_name='Producto', on_delete= models.CASCADE, null= True)
    pantry = models.ForeignKey(Pantry, verbose_name='Alacena', on_delete= models.CASCADE, null= True)
    added_by = models.ForeignKey(User,verbose_name='Creador', on_delete= models.DO_NOTHING, null= True)
    last_update_date = models.DateTimeField('Ultima modificacion', auto_now= True)
    first_update_date = models.DateTimeField('Agregago', auto_now_add= True)
    quantity = models.IntegerField('Cantidad')
    unit = models.CharField('Unidad', choices= Unit.choices, default= Unit.U, max_length=20)
    