from django.db import models

class Tweet(models.Model):
    user_name = models.CharField(max_length=200, blank=True)
    date_tweeted = models.CharField(max_length=25, blank=True)
    tweet = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
