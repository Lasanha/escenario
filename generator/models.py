from django.db import models
import datetime, random
import shutil
import os, escenario.settings
import Image, ImageFont, ImageDraw, textwrap
import pyimgur
IMGUR_API = '804f1fe592b2ce4'


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


    def autonumber(self):
        prefixo = 'NO.' + str(random.randint(1,24))
        self.esc.titulo = prefixo + ' ' + self.esc.titulo


    def prepare(self):
        base = os.path.join(escenario.settings.BASE_DIR, 'escenario_template.jpg')
        alvo = os.path.join(escenario.settings.BASE_DIR, 'tempfiles', self.img_id)
        shutil.copy(base, alvo)
        return alvo


    def draw(self, alvo):
        img = Image.open(alvo)
        font_file = os.path.join(escenario.settings.BASE_DIR, 'ADDWB.TTF')
        font_titulo = ImageFont.truetype(font_file, 20)
        font_faltam = ImageFont.truetype(font_file, 20)
        font_descricao = ImageFont.truetype(font_file, 15)
        linhas = textwrap.wrap(self.esc.descricao, width=33)
        y_text = 92
        draw = ImageDraw.Draw(img)
        draw.text((15,20), self.esc.titulo, (200,200,255), font=font_titulo)
        draw.text((75,60), self.esc.faltam, (100,255,0), font=font_faltam)
        for linha in linhas:
            w, h = font_descricao.getsize(linha)
            draw.text((15, y_text), linha, (200,200,255), font=font_descricao)
            y_text += h + 2
        draw = ImageDraw.Draw(img)
        img.save(alvo)


    def upload(self, alvo):
        im = pyimgur.Imgur(IMGUR_API)
        uploaded_image = im.upload_image(alvo, title=self.esc.titulo)
        os.remove(alvo)
        self.img_id = uploaded_image.link
        self.save()
        

    def __unicode__(self):
        return self.esc.titulo

