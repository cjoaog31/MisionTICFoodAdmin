from rest_framework import serializers
from alacena.models.shoppingList import ShoppingList
from alacena.models.shoppingListProducts import ShoppingListProducts

class shoppingListSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(max_length=20)
    creation_date = serializers.DateTimeField()
    active = serializers.BooleanField()

    #Metadatos, proporciona información sobre el modelo.
    #De forma predeterminada, todos los campos del modelo en la clase se asignarán a los campos del serializador correspondiente.
    class Meta:
        model = ShoppingList
        fields = '__all__'  # Indicamos que incluimos todos los campos del modelo

    #Metodos para devolver instancias de objetos completas en función de datos validados.
    def create(self, validated_data):
        return ShoppingList.objects.create(**validated_data)

    def to_representation(self, instance):
        created_by = instance.created_by
        creation_date = instance.created_by
        active = instance.active

        productosLista = ShoppingListProducts.objects.filter(shopping_list = instance.id)

        return{
            'created_by':created_by,
            'creation_date':creation_date,
            'active':active
        }