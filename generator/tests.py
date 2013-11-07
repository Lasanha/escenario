from django.test import TestCase
from model_mommy import mommy
from models import Esc, EscImg
import os

class EscTest(TestCase):
    def test_esc_creation(self):
        """
        Tests basic esc creation
        """
        esc = mommy.make(Esc)
        self.assertTrue(isinstance(esc,Esc))
        self.assertEqual(esc.__unicode__(), esc.titulo)


    def test_esc_img_creation(self):
        """
        Tests basic esc img creation
        """
        esc_img = mommy.make(EscImg)
        self.assertTrue(isinstance(esc_img, EscImg))
        self.assertEqual(esc_img.__unicode__(), esc_img.esc.titulo)


    def test_esc_img_prepare(self):
        """
        Tests img preparation (copy)
        """
        esc_img = mommy.make(EscImg)
        alvo = esc_img.prepare()
        self.assertTrue(os.path.isfile(alvo))


    def test_esc_img_draw(self):
        """
        Tests img draw
        """
        esc_img = mommy.make(EscImg)
        alvo = esc_img.prepare()
        esc_img.draw(alvo)
        self.assertTrue(os.path.isfile(alvo))


    def test_esc_img_upload(self):
        """
        Tests img upload
        """
        esc_img = mommy.make(EscImg)
        alvo = esc_img.prepare()
        esc_img.draw(alvo)
        esc_img.upload(alvo)
        self.assertTrue('i.imgur.com' in esc_img.img_id)


    def test_esc_img_autonumber(self):
        """
        Tests auto numbering
        """
        esc = mommy.make(Esc)
        esc_img = EscImg(esc=esc)
        esc_img.autonumber()
        esc_img.save()
        self.assertTrue(esc_img.esc.titulo.startswith('NO.'))


    def test_imgur_key_missing(self):
        esc_img = mommy.make(EscImg)
        alvo = esc_img.prepare()
        esc_img.draw(alvo)
        del os.environ['IMGUR_API']
        esc_img.upload(alvo)
        self.assertTrue('i.imgur.com' in esc_img.img_id)
