from alacena.models.product import Product
from alacena.models.wishListProduct import WishListProduct
from rest_framework import serializers
from .wishListProductSerializer import WishListProductSerializer
from authApp.models.user import User


class WishListProductSerializer(serializers.ModelSerializer):
    wishListProduct = WishListProductSerializer()

    class Meta:
        model = WishListProduct
        fields = ['id', 'product', 'added_by',
                  'last_update_date', 'quantity', 'unit']

    def create(self, validated_data):
        userData = validated_data.pop('added_by')
        productData = validated_data.pop('product')
        userInstance = User.objects.filter(username=userData.get('added_by'))
        wishListProductInstance = WishListProduct.objects.create(
            added_by=userInstance, **productData)
        return wishListProductInstance

    def to_representation(self, obj):
        wishListProduct = wishListProduct.objects.get(id=obj.id)
        addedBy = wishListProduct.added_by
        product = wishListProduct.product

        return {
            'id': wishListProduct.id,
            'name': product.name,
            'quantity': wishListProduct.quantity,
            'unit': wishListProduct.get_unit_display(),
            'last_update_date': wishListProduct.last_update_date,
            'added_by': addedBy.username,
        }
