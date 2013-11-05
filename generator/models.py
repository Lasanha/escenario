from django.db import models
import datetime
import shutil
import os, escenario.settings
import Image, ImageFont, ImageDraw

class Esc(models.Model):
    titulo = models.CharField(max_length=30)
    faltam = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)


    def __unicode__(self):
        return self.titulo


class EscImg(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    esc = models.ForeignKey('Esc')
    img_id = models.CharField(max_length=50, default=lambda: str(hash(datetime.datetime.now())) + '.jpg')


    def draw(self):
        base = os.path.join(escenario.settings.BASE_DIR, escenario.settings.STATIC_ROOT, 'escenario_template.jpg')
        alvo = os.path.join(escenario.settings.BASE_DIR, escenario.settings.STATIC_ROOT, self.img_id)
        shutil.copy(base, alvo)
        img = Image.open(alvo)
        font_file = os.path.join(escenario.settings.BASE_DIR, escenario.settings.STATIC_ROOT, 'ADDWB.TTF')
        font_titulo = ImageFont.truetype(font_file, 20)
        font_faltam = ImageFont.truetype(font_file, 20)
        font_descricao = ImageFont.truetype(font_file, 14)
        draw = ImageDraw.Draw(img)
        draw.text((20,20), self.esc.titulo, (200,200,255), font=font_titulo)
        draw.text((80,60), self.esc.faltam, (100,255,0), font=font_faltam)
        draw.text((20,100), self.esc.descricao, (200,200,255), font=font_descricao)
        draw = ImageDraw.Draw(img)
        img.save(alvo)


    def __unicode__(self):
        return self.esc.titulo

