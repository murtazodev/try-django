from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm


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
    context = {
        'form': form,
        'is_update': False,
        'action': 'Create'
    }    

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create_update.html', context)


@login_required
def update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    context = {
        'form': form, 
        'object': obj,
        'is_update': True,
        'action': 'Update'
    }

    if form.is_valid():
        form.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create_update.html', context)


@login_required
def delete_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    if request.method == "POST":
        obj.delete()
        return redirect('recipes:list')
    context = {'object': obj}
    return render(request, 'recipes/delete.html', context)
