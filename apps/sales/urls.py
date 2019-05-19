# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:36
# @Author  : Dzreal93
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

# 配置sales的api
# 1、/sales/api/sales-record 查询销售记录
# 2、/sales/api/sales-record/sales-calc 销售数据计算器
router.register('api/sales-record', SalesRecordViewset, base_name="sales_record_api")
# /sales/api/sales-upload 上传销售记录 api
# router.register('api/sales-upload',SalesUploadViewset, base_name='sales_upload')

urlpatterns = [
    path('sales-upload/', UploadSalesDetailView.as_view(), name="sales_upload"),
    path('sales-record/', SalesRecordView.as_view(), name='sales_record'),
]
urlpatterns += router.urls
