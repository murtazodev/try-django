from django.urls import path
from .views import*

app_name = 'recipes'    

urlpatterns = [
    # path('recipes/recipe-list/', recipe_list_view, name='recipe-list'),
    path('', list_view, name='list'),
    path('create/', create_view, name='create'),
    path('<int:id>/', detail_view, name='detail'),
    path('<int:id>/update/', update_view, name='update'),
    path('<int:id>/delete/', delete_view, name='delete'),
]