from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    runtime = models.IntegerField()
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="like_movies")

class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1,null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, related_name='movie_comments', on_delete=models.CASCADE, blank=True)
    