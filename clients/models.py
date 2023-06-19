from django.db import models             # contains class and methods and functions

# Create your models here

class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateField(auto_now=True)
    email = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)

    # string representation of objects
    def __str__(self):
        return self.first_name
