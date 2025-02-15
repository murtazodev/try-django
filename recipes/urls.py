from django.urls import path
from .views import recipe_list_view, demo

app_name = 'recipes'    

urlpatterns = [
    # path('recipes/recipe-list/', recipe_list_view, name='recipe-list'),
    path('recipe-list/', recipe_list_view, name='recipe_list'),
]