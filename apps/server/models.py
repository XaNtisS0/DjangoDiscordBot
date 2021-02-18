from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=200)
    logging = models.BooleanField(default=True)

    def __str__(self):
        return self.name
