'''
Description: 
Author: Yang Hongzhi
Date: 2021-05-07 14:53:35
'''
from Goods.models import GoodInfo
from django.contrib import admin

# Register your models here.
class GoodInfoAdmin(admin.ModelAdmin):
    list_display=('ID','Name','Price','Company')
    search_fields=('Name',)

admin.site.register(GoodInfo,GoodInfoAdmin)