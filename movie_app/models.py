from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def quantity_movies(self):
        total = 0
        for i in self.movies_count.all():
            if i.title:
                total += 1
        return total


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies_count')

    def __str__(self):
        return self.title

    @property
    def rating(self):
        count = self.movie_reviews.count()
        if count == 0:
            return 0
        total = 0
        for i in self.movie_reviews.all():
            total += i.stars
        return total / count


CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    text = models.TextField(max_length=300)
    stars = models.IntegerField(choices=CHOICES)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name="movie_reviews")

    def __str__(self):
        return self.text
