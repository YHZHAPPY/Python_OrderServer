'''
Description: 
Author: Yang Hongzhi
Date: 2021-04-22 15:31:07
'''
from django.contrib.admin import sites
from login.models import  UserInfo
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User

class OrderServiceAdmin(admin.AdminSite):
     site_title = '仓库订单管理系统'
     # Text to put in each page's <h1>.
     site_header = '订单后台管理系统'

     index_title=''


class UserInfoAdmin(admin.ModelAdmin):
    def GetGender(self):
        if self.Gender==None:
            return "不详"
        elif self.Gender:
            return "男"
        else:
            return "女"
    def GetRole(self):
        if self.Role==0:
            return "普通用户"
        elif self.Role==1:
            return "销售人员"
        elif self.Role==2:
            return "管理人员"
    GetGender.short_description='性别'
    GetRole.short_description='用户类型'
    list_display=('ID','RealName',GetGender,GetRole,'Telephone')
    #搜索项
    search_fields=('RealName','Role','Gender')
    #过了项
    #list_filter=('Role',)

    

class SuperAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff') 

OrderAdmin=OrderServiceAdmin();
admin.site=OrderAdmin
sites.site=OrderAdmin
admin.site.register(User)
admin.site.register(Group)
admin.site.register(UserInfo,UserInfoAdmin)

