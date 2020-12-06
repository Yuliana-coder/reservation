from django.db import models

class Restaurant(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=550)
    address = models.CharField(max_length=200)


def __str__(self):
    return self.title
