from django.contrib import admin
from . import models
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'contenido', 'fecha', 'autor')

admin.site.register(models.BlogPost, BlogAdmin)





