'''
Description: 
Author: Yang Hongzhi
Date: 2021-05-07 14:53:35
'''
from django.db import models
from django.db.models.base import Model

# Create your models here.
class GoodInfo(models.Model):
    class Meta:
        verbose_name ='商品'
        verbose_name_plural = '商品列表'
    ID=models.AutoField(primary_key=True,verbose_name='序号')
    Barcode=models.CharField(max_length=30,verbose_name='商品ID')
    Name=models.CharField(max_length=100,verbose_name='商品名称')
    Price=models.FloatField(default=0,verbose_name="价格")
    ##null=True,blank=True 允许为空
    Company=models.CharField(max_length=10,verbose_name="单位",null=True,blank=True)
    def __str__(self):
        return self.Name

