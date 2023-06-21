from django.db import models             # contains class and methods and functions

# Create your models here

class Transaction(models.Model):
    # users_id = models.CharField(max_length=32)
    payment_method = models.CharField(max_length=32)
    order_id = models.PositiveIntegerField()
    payment_amount = models.DecimalField(max_digits = 6, decimal_places = 2)
    transaction_id = models.PositiveIntegerField()

    # string replesentation of objects
    def __str__(self):
        return self.payment_method
