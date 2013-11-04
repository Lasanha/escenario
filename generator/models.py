from django.db import models

class Esc(models.Model):
    titulo = models.CharField(max_length=30)
    faltam = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.titulo
