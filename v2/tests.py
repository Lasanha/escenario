import vcr
from model_mommy import mommy
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from generator.models import EscImg, MicroblogPost


class V2ApiTests(APITestCase):
    def test_list(self):
        url = reverse('v2:Escenario-list')
        mommy.make(EscImg, _quantity=5)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 5)

    def test_ordering_by_votes(self):
        url = reverse('v2:Escenario-list')
        mommy.make(EscImg, _quantity=5, _fill_optional=['votos'])
        params = {'order_by': '-votos'}
        response = self.client.get(url, data=params)
        self.assertEqual(response.status_code, 200)
        first = response.data['results'][0]
        last = response.data['results'][4]
        self.assertGreater(first['votes'], last['votes'])

    def test_ordering_by_date(self):
        url = reverse('v2:Escenario-list')
        mommy.make(EscImg, _quantity=5)
        params = {'order_by': '-criado_em'}
        response = self.client.get(url, data=params)
        self.assertEqual(response.status_code, 200)
        first = response.data['results'][0]['created_at']
        last = response.data['results'][4]['created_at']
        self.assertGreater(first, last)

    def test_detail(self):
        esc_img = mommy.make(EscImg)
        url = reverse('v2:Escenario-detail', args=(esc_img.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], esc_img.esc.titulo)

    def test_detail_returns_404(self):
        url = reverse('v2:Escenario-detail', args=(9999,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    @vcr.use_cassette('cassettes/v2/api_create.vcr')
    def test_create(self):
        url = reverse('v2:Escenario-list')
        data = {
            'titulo': 'title',
            'faltam': 'remaining',
            'descricao': 'description',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        created_data = response.data
        self.assertEqual(created_data['title'], 'title')
        self.assertEqual(created_data['votes'], 0)

    def test_create_returns_400(self):
        url = reverse('v2:Escenario-list')
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, 400)

    def test_microblog(self):
        mommy.make(MicroblogPost, _quantity=2, fixed=True)
        mommy.make(MicroblogPost, _quantity=1, fixed=False)
        url = reverse('v2:Microblog-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        blog_data = response.data['results']
        self.assertEqual(len(blog_data), 3)
        self.assertEqual(blog_data[0]['fixed'], True)
        self.assertEqual(blog_data[1]['fixed'], False)
        self.assertEqual(blog_data[2]['fixed'], False)
