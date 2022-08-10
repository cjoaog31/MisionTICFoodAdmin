from rest_framework import serializers

from alacena.models.wishListProduct import WishListProduct

class WishListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListProduct
        fields = ["__all__"]

    def create(self, validated_data):
        wish_list_product_instance = WishListProduct.objects.create(**validated_data)
        return wish_list_product_instance

    def to_representation(self, instance):
        response = {
                    "Id": instance.id,
                    "Name": instance.name,
                    "Added By": instance.added_by.username,
                    "Added date": instance.added_date.strftime("%m/%d/%Y %H:%M:%S"),
                    "Quantity": instance.quantity,
                    "Unit": instance.get_unit_display()
        }
        return response
