from django.shortcuts import render
from chambres.models import Chambre



def Home(request):
    context={"chambres":Chambre.objects.all()}
    return render(request,'home.html',context)
