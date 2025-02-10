from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home_view(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})


@login_required
def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article-detail', id=article.id)
    else:
        form = ArticleForm()
    return render(request, 'articles/article_create.html', {'form': form})


def article_detail_view(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'articles/article_detail.html', {'article': article})


def article_update_view(request, id):
    article = Article.objects.get(id=id)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('article-detail', id=article.id)
    return render(request, 'articles/article_update.html', {'form': form, 'article': article})


# def article_create_viewold1(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
    
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
        
#             article_object = Article.objects.create(title=title, content=content)
#             context['object'] = article_object
#             context['created'] = True
#             return redirect('home')
#     return render(request, 'articles/article_create.html', context=context)