from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chambre,Commande,Chalenge
from django.http import HttpResponse
from config.models import Config
import requests
from config.models import Identifiant


# Create your views here.
class SingleChambre(TemplateView):
    def get(self,request,id):
        try:
            if  self.verify_chalenge(request):
                chambre=Chambre.objects.get(id=id)
                return render(request,'chambres/single.html',{'chambre':chambre})
            else:
                return HttpResponse(status=403)
        except:
            return redirect("Home")

    def verify_chalenge(self,request):
        ip=request.META.get("REMOTE_ADDR")
        config=Config.objects.all().first()
        chalenge=Chalenge.objects.last()
        if ip == config.ip or chalenge.result==request.GET.get('ch'):
            Chalenge.objects.filter(ip=ip).delete()
            return True
        else:
            return False





class ChangeEtat(TemplateView):
    def get(self,request,device,commande=1):
        try:
            if  self.verify_chalenge(request):
                device=Commande.objects.get(id=device)
                if commande==1:
                    print(device.commande)
                    device.etat=not device.etat
                    device.save()
                if commande==2:
                    print(device.commande2)
                if commande==3:
                    print(device.commande3)

            else:
                return HttpResponse(status=403)
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=500)


    def verify_chalenge(self,request):
        ip=request.META.get("REMOTE_ADDR")
        config=Config.objects.all().first()
        chalenge=Chalenge.objects.last()
        if ip == config.ip or chalenge.result==request.GET.get('ch'):
            Chalenge.objects.filter(ip=ip).delete()
            return True
        else:
            return False




class NewChalenge(TemplateView):
    def get(self,request):
        chalenge=Chalenge()
        chalenge.create()
        chalenge.ip=request.META.get("REMOTE_ADDR")
        chalenge.save()
        return HttpResponse(chalenge.chalenge)


class InternetSynch(LoginRequiredMixin,TemplateView):
    login=Identifiant.objects.all().first()
    config=Config.objects.all().first()
    internet_chambres=[]
    errors=[]

    def get(self,request):
        self.get_token()
        self.get_chambres()
        self.delete_chambres()
        self.send_chambres()
        self.send_commandes()

        if len(self.errors)>0:
            return render(request,'chambres/error.html',{'errors':errors})
        else:
            return redirect('Home')




    def get_chambres(self):
        try:
            response =requests.get(self.config.site+'/chambres/api',headers=self.headers )
            self.internet_chambres=response.json()
        except Exception as e:
            self.errors.append("erreur lors de la synchronization")




    def delete_chambres(self):
        try:
            if len(self.internet_chambres) > 0:
                for chambre in self.internet_chambres:
                    response =requests.delete(self.config.site+'/chambres/api/'+str(chambre["local_id"]), headers=self.headers )
        except Exception as e:
            self.errors.append("erreur lors de la synchronization")


    def send_chambres(self):
        try:
            for chambre in Chambre.objects.all():
                data={'local_id':chambre.id,"nom":chambre.nom}
                response =requests.post(self.config.site+'/chambres/api',data=data, headers=self.headers )
        except Exception as e:
            self.errors.append("erreur lors de la synchronization")

    def send_commandes(self):
        try:
            for commande in Commande.objects.all():
                data={'local_id':commande.id,
                'nom':commande.nom,
                'type':commande.type,
                'commande':commande.commande,
                'commande2':commande.commande2,
                'commande3':commande.commande3
                }
                response =requests.post(self.config.site+'/chambres/commandes/api/add/'+str(commande.chambre.id), data=data,headers=self.headers )
        except Exception as e:
            print(e)
            self.errors.append("erreur lors de la synchronization")




    def get_token(self):
        try:
            response =requests.post(self.config.site+'/api-auth/', data={'username':self.login.identifiant,'password':self.login.mot_de_passe})
            json=response.json()
            self.token=json['token']
            self.headers={'Authorization': 'Token '+self.token}
        except:
            self.errors.append("erreur lors de l'authentification ")
