from django.urls import path

from . import views 

app_name = 'articles'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.article_create_view, name='create'),
    path('search/', views.article_search_view, name='search'),
    path('<slug:slug>/', views.article_detail_view, name='detail'),
    path('<slug:slug>/update/', views.article_update_view, name='update'),
    # path('index/', views.index_view, name='index'),
    # path('articles', views.articles, name='article-list'),
]