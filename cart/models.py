from django.db import models             # contains class and methods and functions

# Create your models here

class Ecart(models.Model):
    user_id = models.IntegerField()
    total_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    quantity = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    # string replesentation of objects
    def __str__(self):
        return self.user_id