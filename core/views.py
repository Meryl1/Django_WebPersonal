# HttpResponse recibe la peticion y envia la respuesta
from django.shortcuts import render

# Create your views here.

def home(request): #request para realizar la peticion 
    return render(request,"core/home.html") #render=renderiza la peticion

def about(request):
    return render(request,"core/about.html")
def contact(request):
    return render(request,"core/contact.html")