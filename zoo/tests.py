from django.test import TestCase
from zoo import models

class AnimalTestCase(TestCase):

    def test_dog_says(self):
        dog = models.Dog(name='snoopy')
        self.assertEqual(dog.says(), 'woof')
      
      
    def test_cat_says(self):
        cat = models.Cat(name='garfield')
        self.assertEqual(cat.says(), 'meow')

