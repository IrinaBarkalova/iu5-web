from typing import Optional

from django.db import models


class PCMark(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class PCModel(models.Model):
    photo = models.TextField()
    name = models.TextField(unique=True)
    screen = models.FloatField()
    CPU = models.TextField()
    memory = models.TextField()
    price = models.FloatField()
    pc_mark = models.ForeignKey(PCMark, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.photo}, {self.name},{self.screen}, {self.CPU}, {self.memory},{self.price}'
#
#
