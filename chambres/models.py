from django.db import models
from config.models import CleLocal
import string
import secrets
import hmac
import hashlib

# Create your models here.
class Chambre(models.Model):
    nom=models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    class Type(models.TextChoices):
        lampe="Lampe"
        prise="Prise"
        rideau="Rideau"

    nom=models.CharField(max_length=255)
    type=models.CharField(max_length=255,choices=Type.choices)
    commande=models.CharField(max_length=255)
    commande2=models.CharField(max_length=255,blank=True,null=True)
    commande3=models.CharField(max_length=255,blank=True,null=True)
    chambre=models.ForeignKey(Chambre,on_delete=models.CASCADE,blank='true')
    etat=models.BooleanField(default=False)





class Chalenge(models.Model):
    chalenge=models.CharField(max_length=300)
    result=models.CharField(max_length=300)
    ip=models.CharField(max_length=300)
    heure=models.DateTimeField(auto_now_add=True)

    def create(self):
        self.chalenge = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(10))
        cle=str.encode(CleLocal.objects.all().first().cle_local)
        self.result=hmac.new(cle,str.encode(self.chalenge)).hexdigest()
