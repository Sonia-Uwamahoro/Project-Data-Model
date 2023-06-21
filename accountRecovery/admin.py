from django.contrib import admin
from .models import Recover

# Register your models here
class RecoverAdmin(admin.ModelAdmin):
    list_display = ("user_id", "email")


admin.site.register(Recover, RecoverAdmin)







