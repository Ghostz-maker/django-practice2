from django.db import models

# Create your models here.
class Game(models.Model): #made on 27-04-26
    title = models.CharField(max_length=100)
    description = models.TextField()
