from django.contrib import admin
from.models import Transaction

# Register your models here
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("order_id", "payment_method", "payment_amount", "transaction_id")


admin.site.register(Transaction, TransactionAdmin)







