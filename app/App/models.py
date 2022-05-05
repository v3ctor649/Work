from django.db import models

# Create your models here.

class Quiz(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.TextField()
    answer = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
