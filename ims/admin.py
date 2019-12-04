from django.contrib import admin
from .models import *
# Register your models here.

class InventorycalculationAdmin(admin.ModelAdmin):
       
        change_list_template = 'invcal.html' # definitely not 'admin/change_list.html

admin.site.register(Inventorycalculation, InventorycalculationAdmin)

