from django.test import TestCase
from model_mommy import mommy
from generator.models import Esc, EscImg, MicroblogPost
import os
import vcr


class EscTest(TestCase):
    """Testing Escenario model"""
    fixtures = ['users.json']

    def test_esc_creation(self):
        """
        Tests basic esc creation
        """
        esc = mommy.make(Esc)
        self.assertTrue(isinstance(esc, Esc))
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

    @vcr.use_cassette('cassettes/esc_img_upload.vcr')
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
        esc.autonumber()
        self.assertTrue(esc.titulo.startswith('NO.'))

    def test_ec_img_like(self):
        """
        Tests vote feature
        """
        esc_img = mommy.make(EscImg)
        pre = esc_img.votos
        esc_img.like()
        pos = esc_img.votos
        self.assertEqual(pos - pre, 1)

    def test_imgur_key_missing(self):
        """
        Tests behaviour when imgur api key is missing
        """
        esc_img = mommy.make(EscImg)
        alvo = esc_img.prepare()
        esc_img.draw(alvo)
        key = os.environ.get('IMGUR_API')
        os.environ['IMGUR_API'] = ''
        self.assertRaises(Exception, esc_img.upload, alvo)
        os.environ['IMGUR_API'] = key  # restoring

    def test_microblog(self):
        """
        Tests microblog
        """
        micropost_1 = mommy.make(MicroblogPost, fixed=True)
        self.assertTrue(isinstance(micropost_1, MicroblogPost))
        self.assertTrue(micropost_1.fixed)
        micropost_2 = mommy.make(MicroblogPost, fixed=True)
        self.assertTrue(micropost_2.fixed)
        self.assertTrue(isinstance(micropost_2, MicroblogPost))
        self.assertEquals(MicroblogPost.objects.filter(fixed=True).count(), 1)
