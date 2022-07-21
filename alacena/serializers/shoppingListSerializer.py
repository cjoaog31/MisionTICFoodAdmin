from rest_framework import serializers
from alacena.models.shoppingList import ShoppingList
from alacena.models.shoppingListProducts import ShoppingListProducts
from authApp.models.user import User
from .shoppingListSerializer import shoppingListSerializer

class shoppingListSerializer(serializers.ModelSerializer):
    
    shoppingList = shoppingListSerializer()

    #Metadatos, proporciona información sobre el modelo.
    #De forma predeterminada, todos los campos del modelo en la clase se asignarán a los campos del serializador correspondiente.
    class Meta:
        model = ShoppingList
        fields = '__all__'  # Indicamos que incluimos todos los campos del modelo

    #Metodos para devolver instancias de objetos completas en función de datos validados.
    def create(self, validated_data):
        created_by = serializers.CharField(max_length=20)
        creation_date = serializers.DateTimeField()
        active = serializers.BooleanField()

        return ShoppingList.objects.create(**validated_data)

    def to_representation(self, instance):

        #productosLista = ShoppingListProducts.objects.filter(shopping_list = instance.id)
        productsList = ShoppingListProducts.objects.get(id = instance.id)

        return{
            'listProducts': productsList.id,
            'products': productsList.product,
            'quantity': productsList.quantity,
            'unit': productsList.unit, 
            'created_by': instance.created_by,
            'creation_date': instance.created_by,
            'active': instance.active
        }