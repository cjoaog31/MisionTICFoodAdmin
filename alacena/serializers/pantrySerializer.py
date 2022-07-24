from tkinter import INSERT
from rest_framework import serializers

from alacena.models.pantry import Pantry
from authApp.models.user import User

class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = ['id','owner','creation_date', 'last_modification_date', 'replenish_rate']

    def create(self, validated_data):
        pantryInstance = Pantry.objects.create(**validated_data)
        return pantryInstance

    def to_representation(self, instance):
        return {
                    'PantryId': instance.id,
                    'OwnerId': instance.owner.id,
                    'Onwer_Username': instance.owner.username, 
                    'Creation_Date': instance.creation_date.strftime("%m/%d/%Y %H:%M:%S"),
                    'Last_modification_Date': instance.creation_date.strftime("%m/%d/%Y %H:%M:%S"),
                    'Replenish_Rate': instance.replenish_rate
        }
