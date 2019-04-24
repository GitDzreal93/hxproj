"""hxproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.common.views import IndexView
from rest_framework_swagger.views import get_swagger_view
import xadmin

schema_view = get_swagger_view(title='海信项目 API')

urlpatterns = [
    # xadmin
    path('xadmin/', xadmin.site.urls),
    # 首页
    path('', IndexView.as_view(), name="index"),
    path('index/', IndexView.as_view(), name="index"),
    # 公共组件
    path('common/', include('common.urls')),
    # 销
    path('sales/', include('sales.urls')),
    # 进
    path('supply/', include('supply.urls')),
    # 存
    path('stock/', include('stock.urls')),
    # api文档
    path('docs/', schema_view),

]
