from django.shortcuts import render
from django.http import HttpResponse

articles = [
   {
       'id': 1,
       'title': 'First news',
       'text': 'This is the worst first article'
   },
   {
       'id': 2,
       'title': 'Second news',
       'text': 'This is the amazing second article'
   }]

def index(request):
    return render(request, 'news_blog/news_list.html', {'articles':articles})

def get_article(request, article_id):
    article = articles[article_id - 1]
    return render(request, 'news_blog/news_article.html', {'article': article})

def about_autor(reqest):
    return render(reqest, 'news_blog/about.html')

