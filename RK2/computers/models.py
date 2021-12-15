from django.db import models


class PC(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'pc'


class Display(models.Model):
    id = models.IntegerField(primary_key=True)
    matrix_type = models.TextField()
    diagonal = models.FloatField()
    pc = models.ForeignKey(PC, on_delete=models.PROTECT)

    class Meta:
        db_table = 'display'
