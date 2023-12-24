from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import Avatar

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    




class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='uploads/posts/', null=True, blank=True)
    def __str__(self):
        return self.titulo
    
