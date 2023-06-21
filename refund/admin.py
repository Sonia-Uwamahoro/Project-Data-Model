from django.contrib import admin
from .models import Payback

# Register your models here
class PaybackAdmin(admin.ModelAdmin):
    list_display = ("order_id", "refund_id", "amount", "reason")


admin.site.register(Payback, PaybackAdmin)







