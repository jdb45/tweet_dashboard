from django.db import models

class Tweet(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=25)
    # nothing done with this yet
