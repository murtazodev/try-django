from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('index/', views.index_view, name='index'),
    path('article/create/', views.article_create_view, name='article-create'),
    path('article/<int:id>/', views.article_detail_view, name='article-detail'),
    # path('articles', views.articles, name='article-list'),
]