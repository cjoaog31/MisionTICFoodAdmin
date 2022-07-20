from rest_framework import serializers
from alacena.models.wishListProduct import WishListProduct
from alacena.models.shoppingListWishList import ShoppingListWishList

class wishListProductSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(max_length=20)
    creation_date = serializers.DateTimeField()
    active = serializers.BooleanField()

    #Metadatos del modelo.
    class Meta:
        model = WishListProduct
        fields = '__all__'  

    #Metodos para devolver instancias de objetos completas en función de datos validados.
    def create(self, validated_data):
        return WishListProduct.objects.create(**validated_data)

    def to_representation(self, instance):
        created_by = instance.created_by
        creation_date = instance.created_by
        active = instance.active

        return{
            'created_by':created_by,
            'creation_date':creation_date,
            'active':active
        }