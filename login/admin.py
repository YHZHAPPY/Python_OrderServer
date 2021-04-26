'''
Description: 
Author: Yang Hongzhi
Date: 2021-04-22 15:31:07
'''
from login.models import AdminInfo, UserInfo
from django.contrib import admin

class OrderServiceAdmin(admin.AdminSite):
     site_title = '仓库订单管理系统'
     # Text to put in each page's <h1>.
     site_header = '后台管理系统'


class UserInfoAdmin(admin.ModelAdmin):
    list_display=('ID','RealName')
# Register your models here.
# admin.site.register(UserInfo)
OrderAdmin=OrderServiceAdmin();
OrderAdmin.register(AdminInfo)
OrderAdmin.register(UserInfo,UserInfoAdmin)