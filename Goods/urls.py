'''
Description: 
Author: Yang Hongzhi
Date: 2021-05-10 14:27:51
'''
from django.contrib import admin
from django.urls import path
from Goods import views
urlpatterns = [
    path('Add',views.AddGoods),
    path('Remove',views.RemoveGoods),
    path('Modify',views.ModifyGoods),
    path('Get',views.GetGoods),
]