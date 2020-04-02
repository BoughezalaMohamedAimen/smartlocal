from rest_framework import serializers
from .models import Chambre,Commande

class ChambreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chambre
        fields ='__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields ='__all__'
