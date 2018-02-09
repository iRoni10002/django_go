from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Article, Author, Comment


def index(request):
    articles = Article.objects.all().order_by("-published_date")
    return render(request, 'news_blog/news_list.html', {'articles':articles})

def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        author = Author.objects.filter(article__pk=article_id)
        comment = Comment.objects.filter(article=article)
        print("dsfsdfdf:   ", comment)
    except (Article.DoesNotExist, Author.DoesNotExist, Comment.DoesNotExist) as error:
        return HttpResponseNotFound(error)
    return render(request, 'news_blog/news_article.html', {'article': article,
                                                           'autor': author,
                                                           'comment': comment})
    #articles = Article.objects.all()
    #article = articles[article_id - 1]
    #return render(request, 'news_blog/news_article.html', {'article': article})

def about_autor(reqest):
    return render(reqest, 'news_blog/about.html')

