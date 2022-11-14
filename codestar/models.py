from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    
    education = models.CharField(max_length=30)

    level = models.CharField(max_length=10)
    prize = models.CharField(max_length=10)

class Level(models.Model):
    user_id = models.IntegerField()
    level = models.IntegerField()

