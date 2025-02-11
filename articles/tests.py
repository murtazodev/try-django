from django.test import TestCase
from django.utils.text import slugify
from .models import Article
# Create your tests here.
class ArticleTestCase(TestCase):
    def setUp(self):
        self.article1 = Article.objects.create(title='Test Article 1')
        self.article2 = Article.objects.create(title='Test Article 2')
        self.article3 = Article.objects.create(title='Test Article 3')

    def test_article_uniqueness(self):
        self.assertNotEqual(self.article1.slug, self.article2.slug)
        self.assertNotEqual(self.article1.slug, self.article3.slug)

    def test_slug_automatic_generation(self):
        article = Article.objects.create(title='New Article Without Slug')
        expected_slug= slugify(article.title)
        
        self.assertTrue(article.slug.startswith(expected_slug), True)

