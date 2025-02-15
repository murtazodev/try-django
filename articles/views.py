from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def article_search_view(request):
    # query = request.GET.get('q')
    # qs = Article.objects.search(query=query)
    # context ={
    #     'object_list': qs,
    # }
    # return render(request, 'articles/article_search.html', context=context)

    query = request.GET.get('q', '')
    
    if query:
        lookups = Q(title__icontains=query)
        qs = Article.objects.filter(lookups)
    else:
        qs = Article.objects.none()  # Return an empty queryset if no query

    context = {
        'object_list': qs,
        'query': query,
    }
    return render(request, 'articles/search.html', context=context)


def home_view(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})


@login_required
def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect(article.get_absolute_url())
    else:
        form = ArticleForm()
    return render(request, 'articles/create.html', {'form': form})


def article_detail_view(request, slug):
    # Use get_object_or_404 to safely retrieve an article or return a 404 error
    article = get_object_or_404(Article, slug=slug)

    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def article_update_view(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('article-detail', slug=article.slug)
    return render(request, 'articles/update.html', {'form': form, 'article': article})


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