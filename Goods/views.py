'''
Description: 
Author: Yang Hongzhi
Date: 2021-05-07 14:53:35
Django 常用查询API：
1、新增数据：创建对象，赋值后调用save() 方法
2、删除数据：查询得到对象，然后调用delete() 方法
3、修改数据：查询得到对象，修改数据后调用save()方法
4、过滤器：
（1）fiflter 条件语句：查询符合条件的
（2）exclude 条件语句：去除不符合条件
 (3) 条件语句：属性明__运算符=临界值 或者 属性名=值
 运算符：
 gt:大于    lt:小于     gte:大于或等于      lte:小于或等于
 大小写敏感 startswith:以...开头     endswith:以...结尾        contains:包含...        exact:等于...
 前面加上i则是大小写不敏感如：iexact:等于...(不区分大小写)
'''
from django.http.response import HttpResponse
from django.shortcuts import render
from Goods.models import GoodInfo 
# Create your views here.
#新增
def AddGoods(request):
    goods=GoodInfo()
    goods.Barcode='123'
    goods.Name='测试'
    goods.Price=5
    goods.Company='个'
    goods.save()
    return HttpResponse('新增成功')

#删除
def RemoveGoods(request):
    goods=GoodInfo.objects.last()
    goods.delete()
    return HttpResponse('删除成功')

#修改
def ModifyGoods(request):
    goods=GoodInfo.objects.last()
    goods.Name='测试修改'
    goods.save()
    return HttpResponse('修改成功')

def GetGoods(request):
    goods=GoodInfo.objects.filter(Price__gt=2)
    ret=''
    for good in goods:
        ret+=good.Name+"\n"
    return HttpResponse(ret)
    