from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200,verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de cración")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"
        ordering=['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200,verbose_name="Título")
    content=models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="Fecha de publicación",default=timezone.now)
    image=models.ImageField(verbose_name="Imagen",upload_to="blogs",null=True,blank=True)
    author=models.ForeignKey(User,verbose_name="Autor",on_delete = models.CASCADE)
    categories=models.ManyToManyField(Category,verbose_name="Categoria")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de cración")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=['-created']

    def __str__(self):
        return self.title
