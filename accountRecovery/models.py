from django.db import models             # contains class and methods and functions

# Create your models here

class Recover(models.Model):
    user_id = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

        # string replesentation of objects
    def __str__(self):
        return self.user_id
