from django.db import models

# Create your models here.

class Laptop(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram_size = models.PositiveIntegerField()  # in GB
    storage_size = models.PositiveIntegerField()  # in GB
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.brand} {self.model_name}"
