# coding=utf-8

from django.test import TestCase, Client
from django.urls import reverse

from model_mommy import mommy

from vaga.models import VagaModel


class VagaTestCase(TestCase):

    def setUp(self):
        self.url = reverse('vaga:vaga_page')
        self.client = Client()
        self.products = mommy.make('vaga.vaga', _quantity=10)

    def tearDown(self):
        VagaModel.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vaga/vaga_page.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)
        product_list = response.context['vaga']
        self.assertEquals(product_list.count(), 3)
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, 4)

    def test_page_not_found(self):
        response = self.client.get('{}?page=5'.format(self.url))
        self.assertEquals(response.status_code, 404)
