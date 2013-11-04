from django.db import models

class Esc(models.Model):
    titulo = models.TextField(max_length=25)
    faltam = models.TextField(max_length=20)
    descricao = models.TextField(max_length=200)

    def __unicode__(self):
        return self.titulo
