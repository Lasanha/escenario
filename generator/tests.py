from django.test import TestCase
from model_mommy import mommy
from models import Esc, EscImg

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

