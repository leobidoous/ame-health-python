# coding=utf-8

from django.test import Client, TestCase
from django.conf import settings
from django.urls import reverse

from model_mommy import mommy

from pessoa.models import User


class PessoaViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('core:cadastro_gestor')

    def test_register_ok(self):
        data = {
            'username': 'leobidoous', 'password1': 'teste123', 'password2': 'teste123',
            'email': 'test@test.com'
        }
        response = self.client.post(self.register_url, data)
        index_url = reverse('core:perfil')
        self.assertRedirects(response, index_url)
        self.assertEquals(User.objects.count(), 1)

    def test_register_error(self):
        data = {'username': 'leobidoous', 'password1': 'teste123', 'password2': 'teste123'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('core:update_gestor')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_user_ok(self):
        data = {'name': 'test', 'email': 'test@test.com'}
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)
        accounts_index_url = reverse('core:perfil')
        self.assertRedirects(response, accounts_index_url)
        self.user.refresh_from_db()
        self.assertEquals(self.user.email, 'test@test.com')
        self.assertEquals(self.user.name, 'test')

    def test_update_user_error(self):
        data = {}
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdatePasswordTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('core:update_gestor_password')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_password_ok(self):
        data = {
            'old_password': '123', 'new_password1': 'teste123', 'new_password2': 'teste123'
        }
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('teste123'))
