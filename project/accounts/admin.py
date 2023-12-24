from django.contrib import admin
from . import models
# Register your models here.





class AvatarAdmin(admin.ModelAdmin):
    list_display = ('user', 'imagen')

admin.site.register(models.Avatar, AvatarAdmin)


