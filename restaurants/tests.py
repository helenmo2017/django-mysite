from django.test import TestCase
from django.test import client

# Create your tests here.
class IndexWebpageTestCase(TestCase):
	def setUp(self):
		self.c = client.Client()
	def test_index_visiting(self):
		resp = self.c.get('/index/')
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, '<h2> Welcome to my restaurants </h2>')
		self.assertTemplateUsed(resp, 'index.html')