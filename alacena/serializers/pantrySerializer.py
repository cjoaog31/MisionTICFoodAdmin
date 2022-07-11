from rest_framework import serializers
from authApp.models.user import User
from models.pantry import Pantry

class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = ['id','owner','creation_date', 'last_modification_date', 'replenish_Rate']