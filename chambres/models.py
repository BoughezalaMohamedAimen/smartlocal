from django.db import models
import string
import secrets

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
        self.chalenge = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(80))
        numbers=[int(s) for s in self.chalenge if s.isdigit()]
        crypted=''
        i=0
        for s in self.chalenge:

            crypted_char=chr(ord(s)+numbers[i])  if i % 2 ==0 else chr(ord(s)-numbers[i]*2)
            if not crypted_char.isalnum():
                crypted_char=str(ord(crypted_char))
            if numbers[i] % 2 == 0:
                crypted+=crypted_char
            else:
                crypted=crypted_char+crypted

            i+=1
            if(i==len(numbers)):
                i=0
        self.result=crypted
