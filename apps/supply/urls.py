# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:36
# @Author  : Dzreal93
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include, re_path
from .views import *

# urlpatterns 主要用于渲染html，所有数据交互全部交给drf
urlpatterns = [
    path('supply-upload', UploadSupplyDetailView.as_view(), name="supply_upload"),
]
