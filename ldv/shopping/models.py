from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Shopping user
    """
    phone = models.CharField(max_length=10, default="")
    clothes = models.ManyToManyField('Clothe')


class Clothe(models.Model):
    """
    Table de représentation des vêtements
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Clothe"
        verbose_name_plural = "Clothes"
