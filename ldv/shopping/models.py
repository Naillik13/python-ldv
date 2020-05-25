from django.db import models


# Create your models here.

class Clothe(models.Model):
    """
    Table de représentation des vêtements
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=50)