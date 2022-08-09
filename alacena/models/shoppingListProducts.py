from django.db import models
from authApp.models.user import User
from .shoppingList import ShoppingList
from .productPantry import Unit
from .product import Product

class ShoppingListProducts(models.Model):

    shopping_list = models.ForeignKey(ShoppingList, verbose_name='Lista de compras', on_delete= models.CASCADE) 
    product = models.ForeignKey(Product, verbose_name='Producto', on_delete= models.CASCADE)
    quantity = models.IntegerField('Cantidad', default= 1)
    unit = models.CharField('Unidad', choices= Unit.choices, default= Unit.U, max_length= 20)
