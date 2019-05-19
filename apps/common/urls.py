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

# 配置business的api
# router.register('api/business', BusinessViewset, base_name="business_api",basename="business_api")
router.register('api/business', BusinessViewset, base_name="business_api")
router.register('api/store', StoreViewset, base_name="store_api")
router.register('api/product', ProductViewset, base_name="product_api")
router.register('api/upload-file', UploadFileViewset, base_name="upload_file_api")

urlpatterns = [
    path('business/', BusinessView.as_view(), name='business'),
    path('store/', StoreView.as_view(), name='store'),
    path('product/', ProductView.as_view(), name='product'),
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('tmp-download/', DownLoadTemplateFile.as_view(), name='tmp_download'),

    re_path(r'^', include(router.urls)),
]
