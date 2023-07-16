from audioop import avg
from django.db import models

# Create your models here.
class Media(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    image_name= models.CharField(max_length=255,null=True)
    acteurs = models.CharField(max_length=255,null=True)
    realisateur = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    annonce = models.CharField(max_length=255,null=True)
    ratings = []

    def get_average_rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        else:
            return 0
        # ratings = Rating.objects.filter(media_id=self.id)
        # if ratings:
        #     return ratings.aggregate(avg('rating'))['rating__avg']
        # else:
        #     return 0
    def add_img(self, image_name):
        self.image_name = image_name
    def get_img(self):
        if self.image_name == "":
            return None
        else:
            return f'/static/images/{self.image_name}'
    def add_description(self, description):
        self.description = description
    def update_title(self, title):
        self.title = title

class Movie(Media):
    duration = models.IntegerField()
    type = "Movie"

class Series(Media):
    seasons = models.IntegerField()
    type = "Series"

class Rating(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    rating = models.IntegerField()

class Serie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    image_name = models.CharField(max_length=255, null=True)
    acteurs = models.CharField(max_length=255, null=True)
    realisateur = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    annonce = models.CharField(max_length=255, null=True)
    saison = models.CharField(max_length=255, null=True)
    ratings = []

    def add_img(self, image_name):
        self.image_name = image_name

    def get_img(self):
        if self.image_name == "":
            return None
        else:
            return f'/static/images/{self.image_name}'

    def add_description(self, description):
        self.description = description

    def update_title(self, title):
        self.title = title
