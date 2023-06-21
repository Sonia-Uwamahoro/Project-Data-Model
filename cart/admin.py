from django.contrib import admin
from .models import CartProduct

# Register your models here
class CartProductAdmin(admin.ModelAdmin):
    list_display = ("user_id", "products", "total_price", "Quantity", "date_created", "date_updated")


admin.site.register(CartProduct, CartProductAdmin)



