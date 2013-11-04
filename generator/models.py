from django.db import models
import datetime


class Esc(models.Model):
    titulo = models.CharField(max_length=30)
    faltam = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)


    def __unicode__(self):
        return self.titulo


class EscImg(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    esc = models.ForeignKey('Esc')
    img_id = models.CharField(max_length=50, default=lambda: str(hash(datetime.datetime.now())) + 'jpg')


    def draw(self):
        pass


    def __unicode__(self):
        return self.esc.titulo

