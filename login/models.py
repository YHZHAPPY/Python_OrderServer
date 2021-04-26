'''
Description: 
Author: Yang Hongzhi
Date: 2021-04-22 15:31:07
'''
from django.db import models

# Create your models here 用户信息
class  UserInfo(models.Model):
    ID=models.AutoField(primary_key=True)
    OpenID=models.CharField(max_length=50)
    Icon=models.CharField(max_length=200)
    RealName=models.CharField(max_length=50)
    def __str__(self):
        return self.OpenID
#管理员信息
class AdminInfo(models.Model):
    ID=models.AutoField(primary_key=True)
    Account=models.CharField(max_length=50)
    PassWord=models.CharField(max_length=50)
    Power=models.IntegerField()#区分权限

