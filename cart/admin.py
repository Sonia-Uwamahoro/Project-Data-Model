from django.contrib import admin
from .models import Ecart

# Register your models here
class EcartAdmin(admin.ModelAdmin):
    list_display = ("user_id", "total_price", "quantity", "date_created", "date_updated")


admin.site.register(Ecart, EcartAdmin)