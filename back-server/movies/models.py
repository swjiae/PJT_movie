from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=50)

class Credit(models.Model):
    credit_pk = models.AutoField(primary_key=True)
    job = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    profile_path = models.TextField(null=True)
    gender = models.IntegerField()
    character = models.CharField(max_length=100, null=True)
    popularity = models.IntegerField()
    movie_id = models.IntegerField()

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.DateTimeField()
    popularity = models.IntegerField()
    vote_avg = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='genres')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Trailer(models.Model):
    key = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    movie_id = models.IntegerField()

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    score = models.IntegerField()
    content = models.TextField()
    nickname = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    nickname = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    