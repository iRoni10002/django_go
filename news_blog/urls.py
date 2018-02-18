from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path('<int:article_id>/', views.get_article, name='article'),
    path('about', views.about_autor, name='about'),
    path('jopa/', views.new_article, name='new_article'),
    path('<int:article_id>/new', views.new_comment, name='new_comment'),
    path('<int:article_id>/edit', views.edit_article, name='edit'),
]

