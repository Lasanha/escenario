from django.test import TestCase
from model_mommy import mommy
from models import Esc

class EscTest(TestCase):
    def test_esc_creation(self):
        """
        Tests basic test creation
        """
        esc = mommy.make(Esc)
        self.assertTrue(isinstance(esc,Esc))
        self.assertEqual(esc.__unicode__(), esc.titulo)

