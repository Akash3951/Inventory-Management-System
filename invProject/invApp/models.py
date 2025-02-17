from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.name
