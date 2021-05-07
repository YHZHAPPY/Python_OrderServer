'''
Description: 
Author: Yang Hongzhi
Date: 2021-05-07 16:22:36
'''
from enum import Flag
from django.db import models
from django.db.models.aggregates import Count
from django.db.models.base import Model

# Create your models here.
class SaleInfo(models.Model):

    class Meta:
        verbose_name ='订单'
        verbose_name_plural = '订单信息'
    ID=models.AutoField(primary_key=True,verbose_name="订单序号")
    SaleID=models.IntegerField()
    GoodID=models.CharField(max_length=20,verbose_name="商品信息")
    Price=models.FloatField(verbose_name="单价")
    Company=models.CharField(max_length=10,verbose_name="单位")
    Count=models.IntegerField(verbose_name="数量")
    Remarks=models.CharField(max_length=20,verbose_name="备注")
    Flag=models.IntegerField(verbose_name="录入标记")
    def __str__(self):
        return self.ID

class SaleDetails(models.Model): 
    class Meta:
        verbose_name ='订单详情'
        verbose_name_plural = '订单详情列表'
    ID=models.AutoField(primary_key=True,verbose_name="序号")
    CustomerID=models.CharField(max_length=20,verbose_name="商户ID")  
    Time=models.DateTimeField(verbose_name="时间")
    UserName=models.CharField(max_length=10,verbose_name="下单用户")
    Flag=models.IntegerField(verbose_name="录入标记")
    CustomerName=models.CharField(max_length=20,verbose_name="商户名称")
    Amount=models.FloatField(verbose_name="订单金额")