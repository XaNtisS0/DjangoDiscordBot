from django.db import models
import apps.server.models
import apps.rank.models

class User(models.Model):
    username = models.CharField(max_length=200)
    # server that this user is assigned to
    server = models.ForeignKey(apps.server.models.Server, on_delete=models.CASCADE)
    ranks = models.ManyToManyField(apps.rank.models.Rank)

    def __str__(self):
        return self.username
