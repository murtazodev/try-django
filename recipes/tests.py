from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import*
from django.core.exceptions import ValidationError

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='mrt', password='5678m')
    
    def test_user_pswd(self):
        self.assertTrue(self.user_a.check_password('5678m'))

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='mrt', password='5678m')
        self.recipe_a = Recipe.objects.create(name='recipe_a', user=self.user_a)
        self.recipe_b = Recipe.objects.create(name='recipe_b', user=self.user_a)

    def test_user_recipe_reverse_count(self):
        qs = self.user_a.recipe_set.all()
        print(qs.first().name)  
        self.assertEqual(qs.count(), self.user_a.recipe_set.count())

    def test_user_recipe_forward_count(self):
        user = self.user_a 
        qs = Recipe.objects.filter(user=user)
        print(qs.first().name)  
        self.assertEqual(qs.count(), self.user_a.recipe_set.count())

    def test_unit_of_measurement(self):
        ingredient = RecipeIngredient(
            recipe = self.recipe_b,
            name='new ingredient',
            quantity='5',
            unit='lbs',
        )

        ingredient.full_clean()

    def test_unit_of_measurement_error(self):
        invalid_unit = 'nada'
        with self.assertRaises(ValidationError):
            ingredient = RecipeIngredient(
                recipe = self.recipe_b,
                name='new ingredient',
                quantity='5',
                unit=invalid_unit,
            )

            ingredient.full_clean()





