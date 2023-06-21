from django.contrib import admin
from .models import Search

# Register your models here
class SearchAdmin(admin.ModelAdmin):
    list_display = ("user_id", "search_query", "result", "time_stamp")


admin.site.register(Search, SearchAdmin)







