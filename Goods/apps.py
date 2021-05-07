'''
Description: 
Author: Yang Hongzhi
Date: 2021-05-07 14:53:35
'''
from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Goods'
    verbose_name="商品信息"
