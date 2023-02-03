from django.db import models

# Create your models here.

class MyProject(models.Model): #heredo de la clase Model que brinda Django
    title= models.CharField(max_length=200, verbose_name="Titulo")
    description= models.TextField(verbose_name="Descripcion")
    image= models.ImageField(verbose_name="Imagen", upload_to="project") #upload_to donde se iran guardando la multimedia que pertenece al projecto
    link = models.URLField(null=True, blank=True, verbose_name="Enlace")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")  #toma fecha del momento en que se crea         #es necesario agregar estos campos de creacion y actualizacion por buenas practicas
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")      #cambia segun las actualizaciones

    class Meta: #modificaciones extendidas del modelo: cambiar nombre, ordenar registros etc
        verbose_name="Mi proyecto"
        verbose_name_plural="Mis proyectos"
        ordering=["-created"] #- ordena desde el ultimo que se creo hasta el mas antiguo

    def __str__(self): # metodo srt --> retorna en forma de string la informacion del objeto
        return self.title
