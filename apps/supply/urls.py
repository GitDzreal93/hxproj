# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:36
# @Author  : Dzreal93
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

# 配置supply的api
router.register('api/supply-record', SupplyRecordViewset, base_name="supply_record")

# urlpatterns 主要用于渲染html，所有数据交互全部交给drf
urlpatterns = [
    path('supply-upload', UploadSupplyDetailView.as_view(), name="supply_upload"),
    path('supply-record', SupplyRecordView.as_view(), name='supply_record')
]
urlpatterns += router.urls