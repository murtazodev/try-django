from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, RecipeIngredientForm


@login_required
def list_view(request):
    recipes = Recipe.objects.filter(user=request.user)
    context = {'recipes': recipes}
    return render(request, 'recipes/list.html', context)


@login_required
def detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {'object': obj}

    return render(request, 'recipes/detail.html', context)


@login_required
def create_view(request):
    form = RecipeForm(request.POST or None)
    form_2 = RecipeIngredientForm(request.POST or None)
    context = {
        'form': form,
        'is_update': False,
        'action': 'Create'
    }    
    if request.method == 'POST':
        if form.is_valid() and form_2.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            obj_2 = form_2.save(commit=False)
            obj_2.recipe = obj
            obj_2.save()
            return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create_update.html', context)


@login_required
def update_view(request, id=None):
    recipe = get_object_or_404(Recipe, id=id, user=request.user)
    ingredient = recipe.recipeingredient_set.first() or None

    if request.method == 'POST':
        form = RecipeForm(request.POST or None, instance=recipe)
        form_2 = RecipeIngredientForm(request.POST or None, instance=ingredient)
        if form.is_valid() and form_2.is_valid():
            parent = form.save()
            child = form_2.save(commit=False)
            child.recipe = parent
            child.save()
            print('form', form.cleaned_data)
            print('form_2', form_2.cleaned_data)
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm(instance=recipe)
        form_2 = RecipeIngredientForm(instance=ingredient)


        context = {
        'form': form, 
        'form_2': form_2,
        'object': recipe,
        'is_update': True,
        'action': 'Update'
    }
    return render(request, 'recipes/create_update.html', context)
    # context = {
    #     'form': form, 
    #     'form_2': form_2,
    #     'object': recipe,
    #     'is_update': True,
    #     'action': 'Update'


    # if all(form.is_valid(), form_2.is_valid()):
    #     parent = form.save(commit=False)
    #     parent.save()
    #     child = form_2.save(commit=False)
    #     child.recipe = parent
    #     child.save()
    #     print('form', form.cleaned_data)
    #     print('form_2', form_2.cleaned_data)
        
    #     return redirect(recipe.get_absolute_url())
    # return render(request, 'recipes/create_update.html', context)


@login_required
def delete_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    if request.method == "POST":
        obj.delete()
        return redirect('recipes:list')
    context = {'object': obj}
    return render(request, 'recipes/delete.html', context)
