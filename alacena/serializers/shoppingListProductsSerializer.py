from alacena.models.shoppingListProducts import ShoppingListProducts
from rest_framework import serializers


class ShoppingListProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListProducts
        fields = '__all__'

    def create(self, validated_data):
        userData = validated_data.pop('added_by')
        productData = validated_data.pop('product')
        userInstance = User.objects.filter(username= userData.get('added_by'))
        shoppingListProductsInstance = ShoppingListProducts.objects.create(added_by=userInstance, **productData)
        return shoppingListProductsInstance

    def to_representation(self, obj):
        shoppingListProducts = ShoppingListProducts.objects.get(id= obj.id)
        addedBy = shoppingListProducts.added_by
        product = shoppingListProducts.product
        return {
                    'id': ShoppingListProducts.id,
                    'name': product.name,
                    'quantity': ShoppingListProducts.quantity,
                    'unit': ShoppingListProducts.get_unit_display(),
                    'last_update_date': ShoppingListProducts.last_update_date,
                    'added_by': addedBy.username,
        }