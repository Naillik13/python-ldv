from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Shopping user
    """


class Item(models.Model):
    """
    User item
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} for {self.user.username}"


class Product(models.Model):
    """
    Table de représentation des vêtements
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=50)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

