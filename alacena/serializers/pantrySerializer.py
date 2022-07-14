from rest_framework import serializers

from alacena.models.pantry import Pantry

class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = ['id','owner','creation_date', 'last_modification_date', 'replenish_rate']

    def create(self, validated_data):
        pantryInstance = Pantry.objects.create(**validated_data)
        return pantryInstance

    def to_representation(self, instance):
        return super().to_representation(instance)
