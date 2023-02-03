from django.contrib import admin
from .models import MyProject  #.models porque se encuentra dentro del mismo archivo


#Clase para configuracion extendida al administrador crearlo con el nombre del modelo + admin
class MyProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') #solo se visualizan los campos que se especifica, de solo lectura

# Register your models here.
admin.site.register(MyProject, MyProjectAdmin)