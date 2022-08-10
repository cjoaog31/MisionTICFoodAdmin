from django.conf import settings
from django.db import transaction

from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from alacena.models.pantry import Pantry

from alacena.models.userPantryPermission import UserPantryPermission
from alacena.models.product import Product

from .exceptions import IncorrectPantryProduct

class ProductEditView(views.APIView):
    """
    Esta vista se encarga de actualizar los productos de una alacena. Se podrán modificar solo si se cuenta con los permisos necesarios
    acepta varios productos al tiempo o solo uno de ellos, en caso de que el valor llegue a 0 el producto se inactiva
    """

    #DONE

    @transaction.non_atomic_requests
    def post(self, request, *args, **kwargs):
        
        
        try: 
        ##Se encarga de validar el token y de quien es el que está realizando la solicitud
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token, verify=False)

        except:
            stringResponse = {'detail': 'Debe estar logueado para poder realizar esta solicitud'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

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

            productList = request.data.get("ProductList")

            if len(productList) == 0:
                response = {"detail": "No hay modificaciones"}
                return Response(response, status=status.HTTP_304_NOT_MODIFIED)    

            for product in productList:
                productId = product.get("id")
                productInstance = Product.objects.get(id=productId)
                
                # En caso de que la consulta contenga un id de productPantry que no pertenezca al pantry al que se está modificando
                # arrojara un error dado que todos los productos a modificar deben pertenecer a solo una alacena y se debe tener permiso sobre esta
                # para realizar dichos cambios
                if productInstance.pantry.id != pantryId:
                    raise IncorrectPantryProduct("El producto no pertenece al pantry relacionado")
                newQuantity = product.get("quantity")
                if newQuantity == 0:
                    productInstance.active = False
                productInstance.quantity = newQuantity
                productInstance.save()
            response = {"detail": "Se modificaron los productos"}
            return Response(response, status=status.HTTP_200_OK)

        else:
            stringResponse = {'detail': 'No se tiene permiso para realizar esta accion'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request, *args, **kwargs):
        stringResponse = {'detail': 'El metodo get no está habilitado para este endpoint'}
        return Response(stringResponse, status=status.HTTP_400_BAD_REQUEST)