from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name='movies') # Acors에서 Movie 모델 역참조하는 키워드
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

# 브릿지 테이블은 실제로 작성하지는 않음. manytomany fields를 구성하면 자동으로 만들어짐
# class Actor_movies(models.Model):
#     actor_id = models.ForeignKey("movies.Actor", on_delete=models.CASCADE)
#     movie_id = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)