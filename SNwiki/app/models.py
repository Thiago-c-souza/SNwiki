from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class rotinas(models.Model):
    N_rotina = models.CharField(max_length=6)
    Nome_rotina = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.N_rotina +" "+"-"+" "+ self.Nome_rotina

class Post(models.Model):
    Titulo = models.CharField(max_length=255)
    rotina = models.ForeignKey(rotinas, on_delete=models.PROTECT)
    Resumo = RichTextUploadingField()
    