from django.contrib import admin
from .models import Account

# Register your models here
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_name", "email", "first_name", "last_name", "date_of_birth", "phone_number", "address")

admin.site.register(Account, AccountAdmin)

