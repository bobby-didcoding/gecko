from django.contrib import admin
from .models import Pool
 
@admin.register(Pool)
class PoolAdmin(admin.ModelAdmin):
    list_display = ('id','external_id',)
    search_fields = ('external_id',)