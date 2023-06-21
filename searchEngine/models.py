from django.db import models             # contains class and methods and functions

# Create your models here

class Search(models.Model):
    user_id = models.CharField(max_length=32)
    search_query = models.TextField()
    result = models.TextField()
    time_stamp = models.DateTimeField(auto_now = True)
    

    # string replesentation of objects
    def __str__(self):
        return self.user_id
