from django.db import models             # contains class and methods and functions

# Create your models here

class Account(models.Model):
    user_id = models.CharField(max_length=32)
    user_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
  

    # string replesentation of objects
    def __str__(self):
        return self.user_id
