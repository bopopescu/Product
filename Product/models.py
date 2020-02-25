from django.db import models

# Create your models here.
class SearchQuery(models.Model):
    search = models.CharField(max_length=270, null=True)

class Feedback(models.Model):
    email = models.EmailField(max_length=200, null=True)
    question_1 =models.CharField(max_length=40, null=True)
    question_2 = models.CharField(max_length=40, null=True)
    question_3 = models.CharField(max_length=40, null=True)
    question_4 = models.CharField(max_length=40, null=True)
    feedback = models.TextField(max_length=150, null= True)
    prize = models.CharField(max_length=150, null=True)

