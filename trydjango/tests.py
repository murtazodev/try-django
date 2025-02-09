from django.test import TestCase
from django.conf import settings
import os

class TryDjangoConfigTest(TestCase):
    def test_SECRET_KEY_strength(self):
        SECRET_KEY = os.environ.get('SECRET_KEY')
        print(f"SECRET_KEY: {settings.SECRET_KEY}")  # Debugging
        self.assertTrue(len(SECRET_KEY) >= 50)

        # print(f"SECRET_KEY: {settings.SECRET_KEY}")  # Debugging
        # print(f"Length of SECRET_KEY: {len(settings.SECRET_KEY)}")  # Debugging
        # self.assertTrue(len(settings.SECRET_KEY) > 25)
