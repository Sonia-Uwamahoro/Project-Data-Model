from django.contrib import admin
from .models import User

# Register your models here

class UsersAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth", "email", "phone_number")

admin.site.register(User, UsersAdmin)



