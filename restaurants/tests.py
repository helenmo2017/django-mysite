from django.test import TestCase
from django.test import client

# Create your tests here.
class IndexWebpageTestCase(TestCase):
	def setUp(self):
		self.c = client.Client()
	def test_index_visiting(self):
		resp = self.c.post('/restaurants/comment/3/',{'visitor':'test01','email':'mo@mo.mo','content':'it works'})
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, '<h2> Restaurants List </h2>')
		self.assertTemplateUsed(resp, 'comments.html')