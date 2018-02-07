from django.urls import path
from . import views


urlpatterns = [
    path('news', views.index, name='index'),
    path('<int:article_id>/', views.get_article, name='article'),
    path('about', views.about_autor, name='about'),
]

