from django.db import models             # contains class and methods and functions

# Create your models here

class Payback(models.Model):
    order_id = models.CharField(max_length=32)
    refund_id = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits = 6, decimal_places = 2)
    reason = models.TextField()
    # string replesentation of objects
    def __str__(self):
        return self.order_id
