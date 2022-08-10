from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from alacena.models.userPantryPermission import UserPantryPermission

from alacena.models.pantry import Pantry
from alacena.serializers.pantrySerializer import PantrySerializer
from alacena.serializers.userPantryPermissionSerializer import UserPantryPermissionSerializer

class PantryListView(views.APIView):
    """
    Esta vista entrega la lista de pantries a las cuales tiene acceso el usuario conectado, no cuenta con metodo post dado que solo es de consulta
    """

    #DONE
    
    def post(self, request, *args, **kwargs):
        stringResponse = {'detail': 'El metodo post no está habilitado para este endpoint'}
        return Response(stringResponse, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        serializer_class = PantrySerializer
        permission_classes = (IsAuthenticated,)
        try:
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token, verify=False)

            response = {}
            ##This section handles the owned pantry
            user_id = valid_data['user_id']
            queryset = Pantry.objects.get(owner=user_id)
            if queryset is not None:
                serializer = serializer_class(instance=queryset)
                response["owned_Pantry"] = serializer.data
            else:
                response["owned_Pantry"] = "null"

            ##This section handles the pantries where the profile is different
            queryset = UserPantryPermission.objects.filter(user=user_id, active = True)
            pantryList = []
            if len(queryset) > 0:
                for userPantry in queryset:
                    serializer = UserPantryPermissionSerializer(instance=userPantry.pantry)
                    pantryList.append(serializer.data)

            if len(pantryList) > 0:
                response["Other_Pantries"] = pantryList

            return Response(response, status=status.HTTP_200_OK)

        except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
            
