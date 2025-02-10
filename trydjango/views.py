"""
To render html web pages
"""
from articles.models import Article
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
    }

    return render(request, "home-view.html", context=context)