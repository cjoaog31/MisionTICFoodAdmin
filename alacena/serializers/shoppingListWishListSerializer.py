from rest_framework import serializers
from alacena.models.shoppingListWishList import ShoppingListWishList
from .shoppingListWishListSerializer import shoppingListWishListSerializer

class shoppingListWishListSerializer(serializers.ModelSerializer):
    shoppingListWish = shoppingListWishListSerializer()

    class Meta:
        model = ShoppingListWishList
        fields = '__all__'  # Indicamos que incluimos todos los campos del modelo

    def create(self, validated_data):
        shopping_list = ShoppingListWishList.shopping_list
        product = ShoppingListWishList.product
        
        return ShoppingListWishList.objects.create(**validated_data)

    def to_representation(self, instance):
        products = []
        productsWishList = ShoppingListWishList.objects.filter(shopping_Wishlist = instance.id)
        ShopProductSerializer =  shoppingListWishListSerializer(productsWishList, many=True)
        
        for prod in ShopProductSerializer:
            products.add(prod)
        
        return{
            'Name': prod.name,
            'Pantry': prod.pantry,
            'Added_by': prod.added_by,
            'Quantity': prod.quantity
        }
