from django.db import models

# Create your models here.
class SearchQuery(models.Model):
    search = models.CharField(max_length=270, null=True)
