from django.db import models
from authApp.models.user import User
from .shoppingList import ShoppingList
from .wishListProduct import WishListProduct

class ShoppingListWishList(models.Model):

    shopping_list = models.ForeignKey(ShoppingList, verbose_name='Lista de compras', on_delete= models.CASCADE) 
    product = models.ForeignKey(WishListProduct, verbose_name='Producto', on_delete= models.CASCADE)
