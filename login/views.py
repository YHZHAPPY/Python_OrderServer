'''
Description: 
Author: Yang Hongzhi
Date: 2021-04-22 15:31:07
'''
from login.models import UserInfo
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

#用户微信登录
def WeChatLogin(request):
    users=UserInfo.objects.all()
    data={"UserInfo":users}
    return render(request,"admin_details.html",data)

#管理员后台登录
def AdminLogin(request):
    pass