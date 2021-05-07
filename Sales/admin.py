'''
Description: 
Author: Yang Hongzhi
Date: 2021-05-07 16:22:36
'''
from Sales.models import SaleInfo,SaleDetails
from django.contrib import admin

# Register your models here.
class SaleInfoAdmin(admin.ModelAdmin):
    list_display=('ID','GoodID','Price','Company','Count','Remarks','Flag')
class SaleDetailsAdmin(admin.ModelAdmin):
    list_display=('ID','CustomerID','Time','UserName','Flag','CustomerName','Amount')

admin.site.register(SaleInfo,SaleInfoAdmin)
admin.site.register(SaleDetails,SaleDetailsAdmin)
