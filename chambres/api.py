from .models import Chambre,Commande
from .serializers import ChambreSerializer,CommandeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ChambreListApi(APIView):
    """
    List all chambres, or create a new chambre.
    """
    # authentication_classes=(TokenAuthentication,)
    # permission_classes=(IsAuthenticated,)


    def get(self, request, format=None):
        chambres = Chambre.objects.all()
        serializer = ChambreSerializer(chambres, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = ChambreSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CommandeListApi(APIView):
    """
    List all chambres, or create a new chambre.
    """
    # authentication_classes=(TokenAuthentication,)
    # permission_classes=(IsAuthenticated,)


    def get(self, request, format=None):
        commandes = Commande.objects.all()
        serializer = CommandeSerializer(commandes, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = CommandeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
