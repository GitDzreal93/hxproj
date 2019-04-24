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
    path('init-upload/', InitDataView.as_view(), name="init_upload"),
    path('stock-history/', StockHistoryView.as_view(), name="stock_history"),
    path('stock-now/', StockNowView.as_view(), name="stock_now"),
]
