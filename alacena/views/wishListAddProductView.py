from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from alacena.models.pantry import Pantry
from alacena.models.wishListProduct import WishListProduct
from alacena.models.userPantryPermission import UserPantryPermission

from alacena.serializers.wishListProductSerializer import WishListProductSerializer


class wishListAddProductView(views.APIView):
    """
    Esta vista se encarga de adicionar un producto al wishlist de la alacena
    """

    #DONE
    
    def post(self, request, *args, **kwargs):
        serializer_class = WishListProductSerializer
        permission_classes = (IsAuthenticated,)

        try: 
            ##Se encarga de validar el token y de quien es el que está realizando la solicitud
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token, verify=False)

            # ID del usuario realizando la solicitud
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
                
                serializer = WishListProductSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                savedProduct = serializer.save()
                stringResponse = {'detail': 'Se ha adicionado el producto al wishlist correctamente'}           
                return Response(stringResponse, status=status.HTTP_201_CREATED)
            else:
                stringResponse = {'detail': 'No se tiene permiso para realizar esta accion'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request, *args, **kwargs):
        stringResponse = {'detail': 'El metodo get no está habilitado para este endpoint'}
        return Response(stringResponse, status=status.HTTP_400_BAD_REQUEST)