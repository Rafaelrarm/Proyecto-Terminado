from django.test import TestCase
from django.urls import reverse
from mi_app.models import BlogModel
from mi_app.views import BlogList
from django.contrib.auth.models import User
import tempfile


class TestBlog(TestCase):

    def setUp(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        self.user = User.objects.create_user(username='user', email='email@example.com', password='pass')
        self.blog = BlogModel(titulo="titulo", sub_titulo="sub_titulo", cuerpo="cuerpo", autor=self.user)
        self.blog.save()

        self.user_1 = User.objects.create_user(username='user_1', email='email_1@example.com', password='pass')
    
    def test_list_all_blogs(self):
        response = self.client.get(reverse('blog_list'))
        #Cuando se usa class based views se tiene que comprar por el nombre de instancia.
        self.assertEqual(response.resolver_match.func.__name__, BlogList.as_view().__name__)


    
    def test_borrar_blog__usuario_logueado_dueño_blog(self):
        """
        Si el usuario esta logueado y es el dueño del post tiene permisos de borrado.
        El response va a retornar un status_code 200 que significa éxito.
        """

        self.client.login(username='user', password='pass')
        response = self.client.get(reverse('blog_delete',kwargs={'pk':'1'}))
        self.assertEqual(200, response.status_code)
    
    def test_borrar_blog__usario_logueado_no_dueño_del_blog(self):
        """
        Si el usuario esta logueado pero no es el dueño del post, no tiene permisos de borrado.
        El reponse va a retornar un status_code 403 que significa prohibido.
        """
        self.client.login(username='user_1', password='pass')
        response = self.client.get(reverse('blog_delete',kwargs={'pk':'1'}))
        self.assertEqual(403, response.status_code)
