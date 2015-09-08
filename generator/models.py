from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime
import random
import shutil
import os
from PIL import Image, ImageDraw
import textwrap
import pyimgur

F_TITULO = settings.F_TITULO
F_FALTAM = settings.F_FALTAM
F_TEXTO = settings.F_TEXTO
F_WRAP = settings.F_WRAP
font_title = settings.FONT_TITLE
font_text = settings.FONT_TEXT
font_titulo = settings.FONT_TITULO
font_faltam = settings.FONT_FALTAM
font_descricao = settings.FONT_DESCRICAO


class Esc(models.Model):
    titulo = models.CharField(max_length=30)
    faltam = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)

    origem = models.GenericIPAddressField(default='127.0.0.1')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.titulo


def img_default():
    return "%s.jpg" % str(hash(datetime.datetime.now()))


class EscImg(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    esc = models.OneToOneField('Esc')
    img_id = models.CharField(max_length=50, default=img_default)
    votos = models.IntegerField(default=0)

    def autonumber(self):
        prefixo = 'NO.%s' % str(random.randint(1, 24))
        self.esc.titulo = "%s %s" % (prefixo, self.esc.titulo)

    def prepare(self):
        base = os.path.join(settings.BASE_DIR, 'escenario_template.jpg')
        alvo = os.path.join(settings.BASE_DIR, 'tempfiles', self.img_id)
        shutil.copy(base, alvo)
        return alvo

    def draw(self, alvo):
        img = Image.open(alvo)
        linhas = textwrap.wrap(self.esc.descricao, width=F_WRAP)
        y_text = 90
        draw = ImageDraw.Draw(img)
        draw.text((20, 10), self.esc.titulo.upper(), (255, 255, 255), font=font_titulo)
        draw.text((80, 47), self.esc.faltam.upper(), (150, 255, 0), font=font_faltam)
        for linha in linhas:
            h = font_descricao.getsize(linha)[1]
            draw.text((15, y_text), linha, (255, 255, 255), font=font_descricao)
            y_text += h + 2
        draw = ImageDraw.Draw(img)
        img.save(alvo)

    def upload(self, alvo):
        imgur_api = os.environ.get('IMGUR_API', None)
        if not imgur_api:
            raise Exception('IMGUR API missing')
        else:
            im = pyimgur.Imgur(imgur_api)
            uploaded_image = im.upload_image(alvo, title=self.esc.titulo)
            os.remove(alvo)
            self.img_id = uploaded_image.link
            self.save()

    def gostei(self):
        self.votos += 1
        return self.votos 

    def __unicode__(self):
        return self.esc.titulo


class MicroblogPost(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fixed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.fixed:
            others = MicroblogPost.objects.exclude(id=self.id)
            for other in others:
                other.fixed = False
                other.save()
        super(MicroblogPost, self).save(*args, **kwargs)
