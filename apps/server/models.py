from django.db import models

import apps.user.models


class Server(models.Model):
    name = models.CharField(max_length=200)
    logging = models.BooleanField(default=True)
    users = models.ManyToManyField(apps.user.models.User)

    def __str__(self):
        return self.name
