# -*- coding: utf-8 -*-
from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from model_mommy import mommy
from generator.models import Esc, EscImg, MicroblogPost
import os
import time
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
        esc_img = EscImg(esc=esc)
        esc_img.autonumber()
        esc_img.save()
        self.assertTrue(esc_img.esc.titulo.startswith('NO.'))

    def test_ec_img_like(self):
        """
        Tests vote feature
        """
        esc_img = mommy.make(EscImg)
        pre = esc_img.votos
        esc_img.gostei()
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


class ViewsTest(LiveServerTestCase):
    """Testing site views"""
    fixtures = ['users.json']

    def setUp(self):
        """browser setup"""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """browser tear down"""
        self.browser.quit()

    def test_view_home(self):
        """home view test"""
        self.browser.get(self.live_server_url + '/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Fazhe Escenario', body.text)

    @vcr.use_cassette('cassettes/create_escenario.vcr')
    def test_create_escenario(self):
        """create escenario test"""
        self.browser.get(self.live_server_url + '/')
        autonumber = self.browser.find_element_by_name('autonumber')
        autonumber.click()
        titulo = self.browser.find_element_by_name('titulo')
        titulo.send_keys('BLABLABLA')
        faltam = self.browser.find_element_by_name('faltam')
        faltam.send_keys('BLABLABLA')
        descricao = self.browser.find_element_by_name('descricao')
        descricao.send_keys('BLABLABLA')
        descricao.submit()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('FOOORTE GOMBA!!!', body.text)

    def test_view_list(self):
        """list view test"""
        self.browser.get(self.live_server_url + '/list/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('FALTA!! OE PENALTI!!', body.text)
        self.browser.get(self.live_server_url + '/list/?page=20000')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('FALTA!! OE PENALTI!!', body.text)

    def test_view_about(self):
        """about view test"""
        microblog_post = mommy.make(MicroblogPost)
        self.browser.get(self.live_server_url + '/sobre/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('SAC DO GOLERO', body.text)
        self.assertIn(microblog_post.text, body.text)

    def test_view_restricted_and_post_microblog(self):
        """restricted and microblog post view test"""
        self.browser.get(self.live_server_url + '/login/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Username', body.text)
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('teste')
        passwd_field = self.browser.find_element_by_name('password')
        passwd_field.send_keys('teste')
        passwd_field.send_keys(Keys.RETURN)
        # redirected to home
        time.sleep(2)
        # go check restricted
        self.browser.get(self.live_server_url + '/restricted/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('¿QUIEN É ESSE HOME?', body.text)
