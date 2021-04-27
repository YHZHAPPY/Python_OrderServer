'''
Description: 
Author: Yang Hongzhi
Date: 2021-04-22 15:31:07
'''
from django.contrib.admin import sites
from login.models import AdminInfo, UserInfo
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User

class OrderServiceAdmin(admin.AdminSite):
     site_title = '仓库订单管理系统'
     # Text to put in each page's <h1>.
     site_header = '订单后台管理系统'

     index_title=''


class UserInfoAdmin(admin.ModelAdmin):
    list_display=('ID','RealName')

class SuperAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff') 

OrderAdmin=OrderServiceAdmin();
admin.site=OrderAdmin
sites.site=OrderAdmin
admin.site.register(User)
admin.site.register(Group)
admin.site.register(AdminInfo)
admin.site.register(UserInfo,UserInfoAdmin)

