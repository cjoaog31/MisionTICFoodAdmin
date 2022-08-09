from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta, timezone

from alacena.models.pantry import Pantry
from alacena.models.product import Product
from alacena.models.userPantryPermission import UserPantryPermission
from alacena.models.productPantry import ProductPantry
from alacena.models.wishListProduct import WishListProduct
from alacena.serializers.productPantrySerializer import ProductPantrySerializer
from alacena.serializers.productSerializer import ProductSerializer
from alacena.serializers.wishListProductSerializer import WishListProductSerializer

class ShoppingListCreateView(views.APIView):
    
    def get(self, request, *args, **kwargs):
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
                productList = ProductPantry.objects.filter(pantry=pantryId, active=True)
                
                # Valida cada uno de los productos que no se encuentren en 0 y por lo tanto aún estén activos, busca que la ultima actualizacion no supere 3 horas
                # en caso de que esto pase significaria que la alacena está desactualizada y es probable que las cantidades para la
                # lista de compras queden erradas por lo cual es necesario realizar una actualizacion antes de solicitar el calculo
                # de dicha lista de compras 
                now = datetime.now(timezone.utc)
                for product in productList:
                    last_update_date = product.last_update_date
                    diff = (now - last_update_date)
                    hoursDiff = diff.total_seconds() / 3600
                    
                    # En caso de que la ultima actualizacion del status de algún producto de la alacena supere las 3 horas se debe
                    # proceder con la actualizacion de las cantidades antes de poder crear la lista de compras
                    if hoursDiff > 3:
                        stringResponse = {'detail': 'Se debe actualizar primero el estado de los productos'}
                        return Response(stringResponse, status=status.HTTP_412_PRECONDITION_FAILED)
                
                # En caso de que todos los productos se encuentren actualizados se procede a realizar el filtro con respecto a la
                # ultima compra subida al sistema según el refresh rate de la alacena

                refreshRate = ownedPantry.refresh_rate
                delta : datetime

                if refreshRate == 'Q':
                    delta = now - timedelta(days=16)
                else:
                    delta = now - timedelta(days=32)

                lastProductsList = ProductPantry.objects.filter(pantry=pantryId, first_update_date__gte=delta)

                response = {}
                serializedProducts = []
                for product in lastProductsList:
                    serializer = ProductPantrySerializer(instance=product)
                    serializedProducts.append(serializer)
                
                # En caso de que no se hayan agregado productos en el ultimo periodo según el refresh rate se enviara
                # una respuesta vacia / Si se cuentan con productos regresaremos el listado de dichos productos
                response["Suggested_Products"] = serializedProducts

                # Se adiciona la visual de productos que se encuentran en el wishlist

                productWishList = WishListProduct.objects.filter(pantry=pantryId, active=True)
                wishList = []

                for wishProduct in productWishList:
                    serializedWishProduct = WishListProductSerializer(instance=wishProduct)
                    wishList.append(serializedWishProduct.data)
                    
                
                if len(wishList) > 0:
                    response["WishList"] = wishList

                return Response(response, status=status.HTTP_200_OK)

            else:
                stringResponse = {'detail': 'No se tiene permiso para realizar esta accion'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    def create_product(nameString):
        productSearch = Product.objects.filter(name=nameString)

        if len(productSearch) == 0:
            prodDict = {}
            prodDict["name"] = nameString
            serializer = ProductSerializer(data=prodDict)
            serializer.is_valid(raise_exception=True)
            savedProduct = serializer.save()
            return savedProduct.id
        else:
            return productSearch[0].id

    def post(self, request, *args, **kwargs):
        permission_classes = (IsAuthenticated,)
        #try: 
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

            # Se encarga de asegurarse de crear el producto que se agrega a la lista de compras, en caso de que ya existiese y se hubiese por error enviado el ID en null, lo busca y obtiene el ID correcto
            productList = request.data.pop('Product_List')
            for product in productList:
                productId = product.get("productId")
                nameString = product.get("name")
                if productId == "null":
                    update_dict = {}
                    update_dict["productId"] = self.create_product(nameString)
                    product.update(update_dict)
            

            


            stringResponse = {'detail': 'Autorizado'}
            return Response(stringResponse, status=status.HTTP_200_OK)

        else:
            stringResponse = {'detail': 'No se tiene permiso para realizar esta accion'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        """except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        """
