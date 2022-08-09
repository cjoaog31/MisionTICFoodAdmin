from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from alacena.models.pantry import Pantry
from alacena.models.productPantry import ProductPantry
from alacena.models.userPantryPermission import UserPantryPermission
from alacena.models.wishListProduct import WishListProduct

from alacena.serializers.productPantrySerializer import ProductPantrySerializer
from alacena.serializers.wishListProductSerializer import WishListProductSerializer

class DetailPantryProductsView(views.APIView):
    """
    Esta vista muestra el contenido detallado de un pantry en especifico
    """

    #DONE

    def get(self, request, *args, **kwargs):
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
                
                response = {}
                
                productList = ProductPantry.objects.filter(pantry=pantryId, active=True)
                
                serializedProducts = []
                for product in productList:
                    serializer = ProductPantrySerializer(instance=product)
                    serializedProducts.append(serializer)
                
                # En caso de que no se cuente con productos no se agregará nada en la lista
                if len(serializedProducts) > 0:
                    response["ProductList"] = serializedProducts

                productWishList = WishListProduct.objects.filter(pantry=pantryId, active=True)
                wishList = []

                for wishProduct in productWishList:
                    serializedWishProduct = WishListProductSerializer(instance=wishProduct)
                    wishList.append(serializedWishProduct.data)
                    
                # En caso de que no se cuente con productos en el wishlist no se agregará nada en la respuesta
                if len(wishList) > 0:
                    response["WishList"] = wishList

                return Response(response, status=status.HTTP_200_OK)

            else:
                stringResponse = {'detail': 'No se tiene permiso para realizar esta accion'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        stringResponse = {'detail': 'El metodo post no está habilitado para este endpoint'}
        return Response(stringResponse, status=status.HTTP_400_BAD_REQUEST)