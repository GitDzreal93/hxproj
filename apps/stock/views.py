import math
import pandas as pd

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.db.utils import IntegrityError
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.db.models import Avg, Count, Sum

from rest_framework import viewsets, filters, mixins
from rest_framework import status
from rest_framework.decorators import detail_route, list_route, action
from rest_framework.response import Response

from .forms import InitDataUploadForm
from .serializer import StockNowSerializer, StockHistorySerializer
from .filters import StockNowFilter, StockHistoryFilter
from apps.common.views import PageSet
from celery_app.tasks import *
from apps.stock.models import *
from apps.supply.models import *
from apps.sales.models import *


# Create your views here.
class InitDataView(View):
    def get(self, request):
        return render(request, 'init_upload.html')

    def post(self, request):
        initform = InitDataUploadForm(request.POST, request.FILES)
        if initform.is_valid():
            f = request.FILES.get('init_file')
            df = pd.read_excel(f, sheet_name="初期库存导入")
            df.fillna("", inplace=True)
            data_lst = df.to_dict(orient='records')
            input_lst = data_lst
            for input_data in input_lst:
                business_info = Business(business_name=input_data.get("商家名称"), business_code=input_data.get("商家代码"))
                product_info = Product(product_mod=input_data.get("机型"))
                stock_info = Stock(business_id=input_data.get("商家代码"), product_id=input_data.get("机型"),
                                   stock_count=input_data.get("数量"), remarks=input_data.get("备注"), is_init=True)
                # 插入商品表
                try:
                    business_info.save()
                except Exception:
                    return render(request, 'init_upload.html',
                                  {"st": "failed", "errno": 1062, "errmsg": '插入数据库失败', "data": {}})
                # 插入产品表
                try:
                    product_info.save()
                except Exception:
                    return render(request, 'init_upload.html',
                                  {"st": "fail", "errno": 1062, "errmsg": '插入数据库失败', "data": {}})
                # 插入库存表（初始）
                try:
                    if not Stock.objects.filter(business_id=input_data.get("商家代码")):
                        # 库存表的商家信息不能重复
                        stock_info.save()
                except:
                    return render(request, 'init_upload.html',
                                  {"st": "fail", "errno": 1062, "errmsg": '插入数据库失败', "data": {}})
            output_lst = Stock.objects.all().values()
            return render(request, 'init_upload.html',
                          {"err": "suceess", "errno": 0, "errmsg": '', "file_table": input_lst, "db_table": output_lst})


class StockNowViewset(viewsets.ModelViewSet):
    '''
    当前库存记录 API
    '''
    queryset = Stock.objects.all()
    serializer_class = StockNowSerializer
    # 设置分页
    pagination_class = PageSet
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = StockNowFilter
    search_fields = ('business__business_code', 'business__business_name', 'product__product_mod', 'stock_count')
    ordering_fields = ('business_id', 'product_id', 'stock_count')


class StockHistoryViewset(viewsets.ModelViewSet):
    '''
    当前库存记录 API
    '''
    queryset = StockHistory.objects.all()
    serializer_class = StockHistorySerializer
    # 设置分页
    pagination_class = PageSet
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = StockHistoryFilter
    search_fields = ('business__business_code', 'business__business_name', 'product__product_mod','stock_count', 'record_time')
    ordering_fields = ('business_code', 'product_mod', 'stock_count', 'record_time')


class StockNowView(View):
    def get(self, request):
        return render(request, 'hx/stock_now.html')


class StockHistoryView(View):
    def get(self, request):
        return render(request, 'hx/stock_history.html')

