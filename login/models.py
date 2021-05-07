'''
Description: 
Author: Yang Hongzhi
Date: 2021-04-22 15:31:07
'''
from django.db import models
from django.db.models.base import Model

# Create your models here 用户信息
class  UserInfo(models.Model):
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户列表"
    ID=models.AutoField(primary_key=True,verbose_name='序号')
    #微信获取OpenID
    OpenID=models.CharField(max_length=50)
    #头像地址
    Icon=models.CharField(max_length=200)
    #商户信息
    RealName=models.CharField(max_length=50,verbose_name='商户信息',default="")
    #微信的昵称
    NickName=models.CharField(max_length=50)
    Gender=models.NullBooleanField(default=None,verbose_name='性别')
    Telephone=models.CharField(max_length=11,default=None,verbose_name='电话')
    #用户角色
    Role=models.IntegerField(default=0,verbose_name='用户类型')
    def __str__(self):
        return self.NickName
