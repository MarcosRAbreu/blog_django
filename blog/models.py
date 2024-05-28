from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = RichTextField()
    data_publicacao = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.titulo