from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'news_blog/news_list.html', {'articles':articles})

def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'news_blog/news_article.html', {'article': article})
    #articles = Article.objects.all()
    #article = articles[article_id - 1]
    #return render(request, 'news_blog/news_article.html', {'article': article})

def about_autor(reqest):
    return render(reqest, 'news_blog/about.html')

