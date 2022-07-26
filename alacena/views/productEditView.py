from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from alacena.models.pantry import Pantry

from alacena.serializers.productSerializer import ProductSerializer
from alacena.serializers.productPantrySerializer import ProductPantrySerializer
from alacena.models.userPantryPermission import UserPantryPermission
from alacena.models.product import Product
from alacena.models.productPantry import Unit

class productEditView(views.APIView):

     def post(self, request, *args, **kwargs):
        serializer_class = ProductPantrySerializer
        permission_classes = (IsAuthenticated,)
        
        try:

            ##Validar Token
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token, verify=False)

            user_id = valid_data['user_id']

            # Se valida cual es la alacena a la que se quiere realizar cambios y si se cuenta con el permiso necesario
            authorized = False
            pantryId = request.data.get('pantryId')

            ownedPantry = Pantry.objects.filter(id=pantryId)

            if len(ownedPantry) > 0:
                if ownedPantry[0].owner.id == user_id:
                    authorized = True
                else:
                    # Trae todos los permisos de tipo familia que se encuentren activos para cualquier pantry
                    authorizedPantries = UserPantryPermission.objects.filter(pantry=pantryId, active=True, user=user_id, profile='F')
                    if len(authorizedPantries) > 0:
                        authorized = True

            if authorized:    
             
                productId = request.data.pop("productId")

                nameString = request.data.pop("name")
                productSearch = Product.objects.filter(name=nameString)
                
                productId = productSearch[0].id
            
                # response = {}
                # choices = Unit.choices
                # for choice in choices:
                #     response[choice[0]] = choice[1]
                
                request.data["product"] = productId
                
                serializer = serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                stringResponse = {'detail': 'Se ha realizado la modificación con éxito'}
                return Response(stringResponse, status=status.HTTP_201_CREATED)

            else:
                stringResponse = {'detail': 'No se tiene permiso para realizar esta accion'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
