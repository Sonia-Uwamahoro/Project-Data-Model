from django.contrib import admin
from .models import Promotion

# Register your models here
class PromotionAdmin(admin.ModelAdmin):
    list_display = ("product_id", "code", "percentage", "expiry_date", "minimum_purchase")
    
admin.site.register(Promotion, PromotionAdmin)







