from rest_framework import serializers
from alacena.models.pantry import Pantry
from alacena.models.userPantryPermission import UserPantryPermission
from alacena.serializers.pantrySerializer import PantrySerializer
from authApp.models.user import User

class UserPantryPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPantryPermission
        fields = ["__all__"]

    def create(self, validated_data):
        username = validated_data.pop("User")
        userInstance = User.objects.get(username=username)
        pantryID = validated_data.pop("PantryId")
        pantryInstance = Pantry.objects.get(id=pantryID)
        userPermissionInstance = UserPantryPermission.objects.create(user=userInstance, pantry=pantryInstance, **validated_data)
        return userPermissionInstance

    def to_representation(self, instance):
        response = {
                    "Profile": instance.get_pantryprofile_display(),
                    "Permission_Granted_Date": instance.creation_date.strftime("%m/%d/%Y %H:%M:%S"),
                    "Permission_Last_modification Date": instance.last_modification_date.strftime("%m/%d/%Y %H:%M:%S")
        }
        pantrySerializer = PantrySerializer(instance= instance.pantry)

        response.update(pantrySerializer.data)

        return response
