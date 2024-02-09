from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(verbose_name = "Titulo", max_length = 100)
    description = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen", upload_to = 'projects')
    url = models.URLField(verbose_name = "Direccion URL", null = True, blank = True)
    created = models.DateTimeField(verbose_name = "Fecha de creacion", auto_now_add = True)
    updated = models.DateTimeField(verbose_name = "Fecha de Actualizacion", auto_now = True)

    def __str__ (self):
        return self.title
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'