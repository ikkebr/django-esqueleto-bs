from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .views import index

class BaseTests(TestCase):
    def setUp(self):
        self.c = Client()
        
    def teste_raiz_ve_index(self):
        pagina = resolve('/')
        self.assertEqual(pagina.func, index)

    def teste_raiz_retorna_200(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def teste_raiz_nomeada_index_retorna_200(self):
        response = self.c.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def teste_raiz_usa_template_base(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response, "base/index.html")


class LoginTests(TestCase):
    def setUp(self):
        self.c = Client()

    def teste_login_retorna_200(self):
        response = self.c.get(reverse('django.contrib.auth.views.login'))
        self.assertEqual(response.status_code, 200)

    def teste_login_usa_template_correto(self):
        response = self.c.get(reverse('django.contrib.auth.views.login'))
        self.assertTemplateUsed(response, "base/login.html")


class LogoutTests(TestCase):
    def setUp(self):
        self.c = Client()

    def teste_logout_redireciona(self):
        response = self.c.get(reverse('django.contrib.auth.views.logout_then_login'))
        self.assertEqual(response.status_code, 302)


class CadastroTests(TestCase):
    def setUp(self):
        self.c = Client()

    def teste_cadastro_anonimo_retorna_200(self):
        response = self.c.get(reverse("cadastro"))
        self.assertEqual(response.status_code, 200)

    def teste_cadastro_usuario_autenticado_redireciona(self):
        user = User.objects.create_user('dummy', 'dummy@henrique.email', 'dummy')
        self.c.login(username='dummy', password='dummy')
        response = self.c.get(reverse("cadastro"))
        self.assertEqual(response.status_code, 302)

    def teste_cadastro_usa_template_criar(self):
        response = self.c.get(reverse("cadastro"))
        self.assertTemplateUsed(response, "base/criar.html")

    def teste_cadastro_formulario(self):
        response = self.c.get(reverse("cadastro"))
        self.assertEqual( type(response.context['form']), type(UserCreationForm() ))
        
class PerfilTests(TestCase):
    def setUp(self):
        self.c = Client()

    def teste_usuario_anonimo_retorna_302(self):
        response = self.c.get(reverse("perfil"))
        self.assertEqual(response.status_code, 302)

    def teste_usuario_autenticado_retorna_200(self):
        user = User.objects.create_user('dummy', 'dummy@henrique.email', 'dummy')
        self.c.login(username='dummy', password='dummy')
        response = self.c.get(reverse("perfil"))
        self.assertEqual(response.status_code, 200)
