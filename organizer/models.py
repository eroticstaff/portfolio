from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
class Tasks(models.Model):
    name = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    isComplete = models.BooleanField()
