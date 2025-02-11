from django.urls import path

from . import views 

# app_name = 'articles'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('article/create/', views.article_create_view, name='article-create'),
    path('article/search/', views.article_search_view, name='article-search'),
    path('article/<slug:slug>/', views.article_detail_view, name='article-detail'),
    path('article/<slug:slug>/update/', views.article_update_view, name='article-update'),
    # path('index/', views.index_view, name='index'),
    # path('articles', views.articles, name='article-list'),
]