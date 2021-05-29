from django.db import models
import numpy as np
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    #movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING,)
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
