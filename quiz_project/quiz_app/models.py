from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=150)
    choice1 = models.CharField(max_length=50)
    choice2 = models.CharField(max_length=50)
    choice3 = models.CharField(max_length=50)
    choice4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
