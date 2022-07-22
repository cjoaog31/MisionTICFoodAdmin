from rest_framework import serializers
from alacena.models.shoppingListProducts import ShoppingListProducts
from .shoppingListSerializer import shoppingListSerializer
from shoppingListProductsSerializer import ShoppingListProductsSerializer

class shoppingListSerializer(serializers.ModelSerializer):
    
    shoppingList = shoppingListSerializer()

    #Metadatos, proporciona información sobre el modelo.
    #De forma predeterminada, todos los campos del modelo en la clase se asignarán a los campos del serializador correspondiente.
    class Meta:
        model = ShoppingListProducts
        fields = '__all__'  # Indicamos que incluimos todos los campos del modelo

    #Metodos para devolver instancias de objetos completas en función de datos validados.
    def create(self, validated_data):
        created_by = serializers.CharField(max_length=20)
        creation_date = serializers.DateTimeField()
        active = serializers.BooleanField()

        return ShoppingListProducts.objects.create(**validated_data)

    def to_representation(self, instance):
        products = []
        productosLista = ShoppingListProducts.objects.filter(shopping_list = instance.id)
        ShopProductSerializer =  ShoppingListProductsSerializer(productosLista, many=True)
        
        for prod in ShopProductSerializer:
            products.add(prod)

        return{
            'listProducts': instance.id,
            'products': products,
            'created_by': instance.created_by,
            'creation_date': instance.created_by,
            'active': instance.active
        }