from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe


@login_required
def recipe_list_view(request):
    recipes = Recipe.objects.filter(user=request.user)
    context = {'recipes': recipes}
    return render(request, 'recipes/recipe_list.html', context)

def recipe_detail_view(request, id=None):
    pass

def recipe_create_view(request):
    # form=RecipeForm(request.POST or None)
    pass

def recipe_update_view(request, id=None):
    pass
