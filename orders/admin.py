from django.contrib import admin
from .models import UserOrder

# Register your models here
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ("user_id", "products", "total_price", "shipping_address", "date_created", "date_updated")


admin.site.register(UserOrder, UserOrderAdmin)



