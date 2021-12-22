from django.db import models


class PCModel(models.Model):
    photo = models.TextField()
    name = models.TextField(unique=True)
    screen = models.FloatField()
    CPU = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    price = models.FloatField()
