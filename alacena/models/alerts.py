from django.db import models
from authApp.models.user import User
from .pantry import Pantry
from .product import Product

class Alerts(models.Model):

    pantry = models.ForeignKey(Pantry, verbose_name='Alacena', on_delete= models.CASCADE, null= True)
    product = models.ForeignKey(Product, verbose_name='Producto', on_delete= models.CASCADE, null= True)
    alert_date = models.DateTimeField('Añadido', auto_now_add= True)
    read = models.BooleanField('Activa', default= True)