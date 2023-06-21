from django.db import models             # contains class and methods and functions

# Create your models here

class Notice(models.Model):
    user_id = models.CharField(max_length=32)
    message = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add = True)
    
    # string replesentation of objects
    def __str__(self):
        return self.user_id
