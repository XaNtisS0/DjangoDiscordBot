from django.db import models
import apps.server.models
import apps.rank.models

class User(models.Model):
    username = models.CharField(max_length=200)
    ranks = models.ManyToManyField(apps.rank.models.Rank)

    def __str__(self):
        return self.username
