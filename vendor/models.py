from django.db import models             # contains class and methods and functions

# Create your models here

class Seller(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    products = models.CharField(max_length=32)
    # string replesentation of objects
    def __str__(self):
        return self.name
