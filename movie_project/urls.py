from django.urls import path
from movie_test import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='index'),
    path('films/', views.films, name='films'),
    path('series/', views.series, name='series'),
    path('contact/', views.contact, name='contact'),
    path('media_detail/<int:Media_id>/', views.film_detail, name='film_detail'),
    path('serie_detail/<int:id>/', views.serie_detail, name='serie_detail'),
    path('media/genre/<str:movie_genre>/', views.film_genre, name='media_genre'),
    path('media/year/<str:movie_year>/', views.film_year, name='media_year'),
    path('media/acteurs/<str:movie_acteurs>/', views.film_acteurs, name='media_acteurs'),
    path('media/realisateur/<str:movie_realisateur>/', views.film_realisateur, name='media_realisateur'),
    path('media/annonce/<str:movie_annonce>/', views.film_annonce, name='media_annonce'),
]
