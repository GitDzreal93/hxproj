# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:36
# @Author  : Dzreal93
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('business', BusinessView.as_view(), name='business'),
    path('store', StoreView.as_view(), name='store'),
    path('product', ProductView.as_view(), name='product')
]
