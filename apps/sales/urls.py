# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 20:36
# @Author  : Dzreal93
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.contrib import admin
from django.urls import path,include,re_path
from .views import *

view_patterns = [

]

api_patterns = [

]

urlpatterns = [
    path('view/', include(view_patterns)),
    path('api/', include(api_patterns)),
]
