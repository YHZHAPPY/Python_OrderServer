'''
Description: 
Author: Yang Hongzhi
Date: 2021-04-22 15:31:07
'''
from django.apps import AppConfig


class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'
    verbose_name="用户信息"
