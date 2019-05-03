# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:36
# @Author  : Dzreal93
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

# 配置sales的api
# 1、/stock/api/stock-now 查询当前库存记录
router.register('api/stock-now', StockNowViewset, base_name="stock_now")
router.register('api/stock-history', StockHistoryViewset, base_name="stock_history")

urlpatterns = [
    path('init-upload/', InitDataView.as_view(), name="init_upload"),
    path('stock-history/', StockHistoryView.as_view(), name="stock_history"),
    path('stock-now/', StockNowView.as_view(), name="stock_now"),
]
urlpatterns += router.urls