from django.db import models
import numpy as np



# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)

    def average_rating(self):
        all_rating = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

        def _unicode_(self):
            return self.name

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    #movie = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)

