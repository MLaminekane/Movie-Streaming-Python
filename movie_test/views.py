from django.shortcuts import render
from movie_test.models import Media, Movie, Series, Serie


# Create your views here.
def index(request):
    media = Media.objects.all()
    return render(request, 'index.html', {'Media':media,'test':media[0],'test2':media[0].get_img(),'test3':media[0].get_average_rating()})
def films(request):
    media = Movie.objects.all()
    return render(request, 'films.html',{'Media':media})
def series(request):
    media = Series.objects.all()
    return render(request, 'series.html',{'Media':media})
def film_detail(request, Media_id):
    media = Media.objects.get(id=Media_id)
    return render(request, 'media_detail.html', {'Media': media})
def serie_detail(request, id):
    serie = Serie.objects.get(id=id)
    return render(request, 'serie_detail.html', {'Serie': serie})
def film_genre(request, movie_genre):
    media = Media.objects.filter(genre=movie_genre)
    return render(request, 'media_genre.html', {'Media': media})
def film_year(request, movie_year):
    media = Media.objects.filter(year=movie_year)
    return render(request, 'media_year.html', {'Media': media})
def film_acteurs(request, movie_acteurs):
    media = Media.objects.filter(acteurs=movie_acteurs)
    return render(request, 'media_acteurs.html', {'Media': media})
def film_realisateur(request, movie_realisateur):
    media = Media.objects.filter(realisateur=movie_realisateur)
    return render(request, 'media_realisateur.html', {'Media': media})
def film_annonce(request, movie_annonce):
    media = Media.objects.filter(annonce=movie_annonce)
    return render(request, 'media_annonce.html', {'Media':media})
def contact(request):
    return render(request, 'contact.html')