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

class productAddView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer_class = ProductPantrySerializer
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
                # Se encarga de validar si el producto existe o no en la base de datos
                # En caso de que no exista lo crea y si lo llega a encontrar hace una referencia a él para evitar duplicar 
                productId = request.data.pop("productId")
                
                if productId == "null":

                    nameString = request.data.pop("name")
                    productSearch = Product.objects.filter(name=nameString)

                    if len(productSearch) == 0:
                        prodDict = {}
                        prodDict["name"] = nameString
                        serializer = ProductSerializer(data=prodDict)
                        serializer.is_valid(raise_exception=True)
                        savedProduct = serializer.save()
                        productId = savedProduct.id
                    else:
                        productId = productSearch[0].id

                request.data["product"] = productId
                request.data["added_by"] = user_id
                request.data["pantry"] = pantryId

                serializer = serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                stringResponse = {'detail': 'Se ha adicionado el producto solicitado'}
                return Response(stringResponse, status=status.HTTP_201_CREATED)

            else:
                stringResponse = {'detail': 'No se tiene permiso para realizar esta accion'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request, *args, **kwargs):
        querySet = Product.objects.all()
        serializer_class = ProductSerializer
        permission_classes = (IsAuthenticated,)
        try:
            ##Se encarga de validar el token y de quien es el que está realizando la solicitud
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token, verify=False)
            
            response = {}

            if len(querySet) > 0:
                productList = []
                for product in querySet:
                    productSerialized = serializer_class(product)
                    productList.append(productSerialized.data)

                response["Product_List"] = productList
            

            unitList = {}

            choices = Unit.choices
            for choice in choices:
                unitList[choice[0]] = choice[1]

            response["Units"] = unitList
            
            return Response(response, status=status.HTTP_200_OK)
        except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)