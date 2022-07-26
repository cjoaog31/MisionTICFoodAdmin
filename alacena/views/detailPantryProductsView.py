from urllib import response
from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from alacena.models.productPantry import ProductPantry
from alacena.serializers.productPantrySerializer import ProductPantrySerializer

class detailPantryProducts(views.APIView):
    def get(self, request, *args, **kwargs):
        querySet = ProductPantry.objects.all()
        serializer_class = ProductPantrySerializer

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        respose = {}

        productPantrySerializerList = serializer_class(data=querySet, many=True)
        
        if len(productPantrySerializerList != 0):
            response["productPantryList"] = productPantrySerializerList
        else:
            response["productPantryList"] = "null"

        return Response(response, status.HTTP_200_OK)