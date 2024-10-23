from django.test import TestCase
from .models import Address

# Create your tests here.
class AnimalTestCase(TestCase):
    def setUp(self):
        Address.objects.create(city="lion")
        Address.objects.create(city="cat")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Address.objects.get(city="lion")
        cat = Address.objects.get(city="cat")
       
     