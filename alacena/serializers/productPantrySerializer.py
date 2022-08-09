from alacena.models.productPantry import ProductPantry
from rest_framework import serializers

class ProductPantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPantry
        fields = ['id','product', 'added_by', 'last_update_date', 'first_update_date', 'quantity', 'unit', 'pantry', 'expiration_date']

    def create(self, validated_data):
        productPantryInstance = ProductPantry.objects.create(**validated_data)
        return productPantryInstance

    def to_representation(self, obj):
        productPantry = obj
        addedBy = productPantry.added_by
        product = productPantry.product
        return {
                    'id': productPantry.id,
                    'name': product.name,
                    'quantity': productPantry.quantity,
                    'unit': productPantry.get_unit_display(),
                    'last_update_date': productPantry.last_update_date,
                    'added_by': addedBy.username,
                    'first_update_date': productPantry.first_update_date
        }