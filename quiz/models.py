from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length = 201)
    body = models.TextField()
    answer = models.IntegerField()
# Create your models here.
