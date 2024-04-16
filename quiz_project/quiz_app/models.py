from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=150)
    choice1 = models.CharField(max_length=50)
    choice2 = models.CharField(max_length=50)
    choice3 = models.CharField(max_length=50)
    choice4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

class Player(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    score = models.IntegerField(default=0)
