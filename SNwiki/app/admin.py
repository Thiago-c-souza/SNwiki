from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.rotinas)
admin.site.register(models.Tipo_erro)
