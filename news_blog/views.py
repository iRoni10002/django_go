from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Article, Author, Comment
from .forms import ArticleForm, CommentForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404


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
                                                           'author': author,
                                                           'comment': comment})
    #articles = Article.objects.all()
    #article = articles[article_id - 1]
    #return render(request, 'news_blog/news_article.html', {'article': article})

def about_autor(reqest):
    return render(reqest, 'news_blog/about.html')

def new_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('article', article_id=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'news_blog/edit_article.html', {'form': form})


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('article', article_id=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'news_blog/edit_article.html', {'from': form}
                       )




def new_comment(request, article_id):
   if request.method == "POST":
       form = CommentForm(request.POST)
       if form.is_valid():
           comment = form.save(commit=False)
           comment.published_date = timezone.now()
           comment.save()
           return redirect('comment', article_id = Article.objects.get(id = article_id))
   else:
       form = CommentForm()
   return render(request, 'news_blog/edit_comment.html', {'form': form})
