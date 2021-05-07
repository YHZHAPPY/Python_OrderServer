'''
Description: 
Author: Yang Hongzhi
Date: 2021-05-07 16:22:36
'''
from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Sales'
    verbose_name="订单信息"
