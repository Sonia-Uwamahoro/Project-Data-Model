from django.db import models             # contains class and methods and functions

# Create your models here

class Promotion(models.Model):
    product_id = models.CharField(max_length=32)
    code = models.IntegerField(default=0)
    percentage = models.DecimalField(max_digits = 6, decimal_places = 2)
    expiry_date = models.DateField(auto_now=True)
    minimum_purchase = models.DecimalField(max_digits = 6, decimal_places = 2)
    
    # string replesentation of objects
    def __str__(self):
        return self.product_id
