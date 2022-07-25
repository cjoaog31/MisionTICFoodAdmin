from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from alacena.models.pantry import Pantry, ReplenishRate
from alacena.serializers.pantrySerializer import PantrySerializer

class PantryCreateView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        queryset = Pantry.objects.all()
        serializer_class = PantrySerializer
        permission_classes = (IsAuthenticated,)
        #Confirmar el token
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        user_id = valid_data['user_id']

        pantryInstance = queryset.filter(owner=user_id)

        if len(pantryInstance) != 0:
            stringResponse = {'detail': 'Este usuario ya cuenta con una alacena'}
            return Response(stringResponse,status=status.HTTP_405_METHOD_NOT_ALLOWED)

        request.data['owner'] = user_id

        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        ##TODO
        return Response(request.data)

    def get(self, request, *args, **kwargs):
        permission_classes = (IsAuthenticated,)
        try:
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token, verify=False)

            response = {}
            choices = ReplenishRate.choices
            for choice in choices:
                response[choice[0]] = choice[1]
            return Response(response, status=status.HTTP_200_OK)

        except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
            
