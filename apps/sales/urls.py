# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:36
# @Author  : Dzreal93
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.contrib import admin
from django.urls import path,include,re_path
from .views import *


urlpatterns = [
    path('sales-upload', UploadSalesDetailView.as_view(), name="sales_upload"),
    path('sales-record', SalesRecordView.as_view(), name='sales_record'),
]
