from django.contrib import admin
from .models import Seller

# Register your models here
class SellerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "address", "products")


admin.site.register(Seller, SellerAdmin)







