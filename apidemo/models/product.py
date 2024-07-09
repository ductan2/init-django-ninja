from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

