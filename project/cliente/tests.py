from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost


class BlogPostTestCase(TestCase):
    def setUp(self):
        # Configurar cualquier dato inicial
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_blog_post(self):
        """
        Caso de Prueba: Crear una nueva entrada de blog

        Descripción:
        Verificar que se pueda crear y guardar una nueva entrada de blog en la base de datos.

        Datos de Prueba:
        - Título: "Test Blog Post"
        - Subtitulo: "Subtitulo para la entrada de prueba"
        - Contenido: "Este es el contenido de la entrada de prueba."

        Resultado Esperado:
        La entrada de blog se crea con exito y sus atributos coinciden con los datos de entrada.
        """

        # Organizar
        datos_entrada_blog = {
            'titulo': 'Test Blog Post',
            'subtitulo': 'Subtitulo para la entrada de prueba',
            'contenido': 'Este es el contenido de la entrada de prueba.',
            'autor': self.user,
        }

        # Actuar
        entrada_blog = BlogPost.objects.create(**datos_entrada_blog)

        # Afirmar
        self.assertEqual(entrada_blog.titulo, datos_entrada_blog['titulo'])
        self.assertEqual(entrada_blog.subtitulo, datos_entrada_blog['subtitulo'])
        self.assertEqual(entrada_blog.contenido, datos_entrada_blog['contenido'])
        self.assertEqual(entrada_blog.autor, datos_entrada_blog['autor'])
        self.assertIsNotNone(entrada_blog.fecha)

    def test_blog_post_str_method(self):
        """
        Caso de Prueba: Método __str__ de la entrada de blog

        Descripción:
        Verificar que el método __str__ de la entrada de blog devuelva la representación en cadena correcta.

        Resultado Esperado:
        El método __str__ devuelve el título de la entrada de blog.
        """

        # Organizar
        entrada_blog = BlogPost(titulo='Test Blog Post', autor=self.user)

        # Actuar
        resultado = str(entrada_blog)

        # Afirmar
        self.assertEqual(resultado, 'Test Blog Post')

    def test_blog_post_field_constraints(self):
        """
        Caso de Prueba: Restricciones de campo para la entrada de blog

        Descripción:
        Verificar que los campos del modelo de la entrada de blog tengan las restricciones y validaciones esperadas.

        Resultado Esperado:
        Las restricciones de campo se aplican como se espera.
        """

        # Organizar
        # Agregar escenarios de prueba para verificar restricciones de campo, por ejemplo, max_length, null, blank, etc.

        # Actuar y Afirmar
        # Escribir afirmaciones para verificar restricciones de campo para titulo, subtitulo, contenido, etc.
