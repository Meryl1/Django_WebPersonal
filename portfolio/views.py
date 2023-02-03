# HttpResponse recibe la peticion y envia la respuesta
from django.shortcuts import render
from .models import MyProject



def portfolio(request):
    #obtener la lista de proyectos almacenados
    project=MyProject.objects.all()
    return render(request,"portfolio/portfolio.html", {'project':project})

