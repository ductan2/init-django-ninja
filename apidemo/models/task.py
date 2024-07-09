from django.db import models
from .product import Product


class Task(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField()
