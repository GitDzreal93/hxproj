# -*- coding:utf-8 -*-
from __future__ import absolute_import
import json
from dateutil.parser import parse
import pandas as pd
import math
from pprint import pprint

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.db.models import Avg, Count, Sum

from rest_framework import viewsets, filters, mixins
from rest_framework import status
from rest_framework.decorators import detail_route, list_route, action
from rest_framework.response import Response

from .forms import UploadSalesDetailForm
from apps.sales.models import SalesRecord
from apps.common.models import Business, Product, Store
from apps.common.views import PageSet
from apps.sales.serializer import SalesRecordSerializer, SalesCalcSerializer
from apps.sales.filters import SalesRecordFilter


class UploadSalesDetailView(View):
    def get(self, request):
        return render(request, 'sales_upload.html')

    def post(self, request):
        '''导入供货信息'''
        supply_file = UploadSalesDetailForm(request.POST, request.FILES)
        if supply_file.is_valid():
            f = request.FILES.get('sales_file')
            df = pd.read_excel(f, sheet_name="销售数据导入")
            df.fillna("", inplace=True)
            data_lst = df.to_dict(orient='records')
            for input_data in data_lst:
                business_code = input_data.get("商家代码")
                business_name = input_data.get("商家名称")
                store_code = input_data.get("门店代码")
                store_name = input_data.get("门店名称")
                product_mod = input_data.get("型号")
                sales_time = parse(input_data.get("时间")) if type(input_data.get("时间")) == int else input_data.get("时间")
                retail_sales = input_data.get("零售销量")
                retail_price = float(input_data.get("实际零售金额"))
                project_sales = input_data.get("工程销量")
                project_price = float(input_data.get("实际工程金额"))
                wholesale_sales = input_data.get("批发销量")
                wholesale_price = float(input_data.get("实际批发金额"))
                online_sales = input_data.get("电商销量")
                online_price = float(input_data.get("实际电商金额"))
                data_src = input_data.get("数据来源")
                # 假如没有商家信息的话，就插入商家信息
                try:
                    Business.objects.get(business_code=business_code)
                except Business.DoesNotExist:
                    Business(
                        business_code=business_code,
                        business_name=business_name
                    ).save()
                # 假如没有门店信息的话，就插入门店信息
                try:
                    Store.objects.get(store_code=store_code)
                except Store.DoesNotExist:
                    Store(
                        business_id=business_code,
                        store_code=store_code,
                        store_name=store_name,
                    ).save()
                # 假如没有产品型号信息的话，就插入产品
                try:
                    Product.objects.get(product_mod=product_mod)
                except Product.DoesNotExist:
                    Product(
                        product_mod=product_mod
                    ).save()
                # 插入销售明细
                SalesRecord(
                    business_id=business_code,
                    store_id=store_code,
                    product_id=product_mod,
                    sales_time=sales_time,
                    retail_sales=retail_sales,
                    retail_price=retail_price,
                    project_sales=project_sales,
                    project_price=project_price,
                    wholesale_sales=wholesale_sales,
                    wholesale_price=wholesale_price,
                    online_sales=online_sales,
                    online_price=online_price,
                    data_src=data_src,
                ).save()
            queryset = list(SalesRecord.objects.all().values())
            return render(request, 'sales_upload.html', {"formlist": data_lst, "querydata": queryset})


class SalesRecordViewset(viewsets.ModelViewSet):
    '''
    销售记录 API
    '''
    queryset = SalesRecord.objects.all()
    serializer_class = SalesRecordSerializer
    # 设置分页
    pagination_class = PageSet
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = SalesRecordFilter
    search_fields = ('business_id', 'store_id', 'product_id')
    ordering_fields = ('business_id', 'store_id', 'product_id', 'sales_time')

    @list_route(methods=['get'])
    def sales_calc(self, request):
        filter_class = self.filter_class
        f = filter_class(request.GET, queryset=SalesRecord.objects.all())
        qs = f.qs
        calc_result = dict(
            bussiness_count = qs.values('business_id').distinct().count(),
            store_count = qs.values('store_id').distinct().count(),
            product_count = qs.values('store_id').distinct().count(),
            retail_total_sales = qs.aggregate(Sum('retail_sales')).get('retail_sales__sum', 0),
            retail_total_price = qs.aggregate(Sum('retail_price')).get('retail_price__sum', 0),
            project_total_sales = qs.aggregate(Sum('project_sales')).get('project_sales__sum', 0),
            project_total_price = qs.aggregate(Sum('project_price')).get('project_price__sum', 0),
            wholesale_total_sales = qs.aggregate(Sum('wholesale_sales')).get('wholesale_sales__sum', 0),
            wholesale_total_price = qs.aggregate(Sum('wholesale_price')).get('wholesale_price__sum', 0),
            online_total_sales = qs.aggregate(Sum('online_sales')).get('online_sales__sum', 0),
            online_total_price = qs.aggregate(Sum('online_price')).get('online_price__sum', 0),
        )
        serializer = SalesCalcSerializer(calc_result)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SalesRecordView(View):
    def get(self, request):
        queryset = SalesRecord.objects.all()
        data = {}
        data["title"] = dict(
            business='商家信息',
            store='门店信息',
            product='产品信息',
            retail='零售',
            project='工程',
            wholesale='批发',
            online='电商'
        )
        sales_lst = []
        for sales in queryset.values():
            # 获取商家信息
            business_code = sales.get("business_id")
            business_query = Business.objects.filter(business_code=business_code).values('business_name')
            business_name = business_query[0].get("business_name")
            # 获取门店信息
            store_code = sales.get("store_id")
            store_query = Store.objects.filter(store_code=store_code).values('store_name')
            store_name = store_query[0].get("store_name")
            # 产品型号
            product_mod = sales.get("product_id")
            sales_dict = dict(
                business_name=business_name,
                business_code=business_code,
                store_name=store_name,
                store_code=store_code,
                product_mod=product_mod,
                retail_sales=sales.get("retail_sales"),
                retail_price=sales.get("retail_price"),
                project_sales=sales.get("project_sales"),
                project_price=sales.get("project_price"),
                wholesale_sales=sales.get("wholesale_sales"),
                wholesale_price=sales.get("wholesale_price"),
                online_sales=sales.get("online_sales"),
                online_price=sales.get("online_price"),
            )
            sales_lst.append(sales_dict)
        data["sales_lst"] = sales_lst
        retail_sales_list = queryset.values_list('retail_sales', flat=True)
        retail_price_list = queryset.values_list('retail_price', flat=True)
        project_sales_list = queryset.values_list('project_sales', flat=True)
        project_price_list = queryset.values_list('project_price', flat=True)
        wholesale_sales_list = queryset.values_list('wholesale_sales', flat=True)
        wholesale_price_list = queryset.values_list('wholesale_price', flat=True)
        online_sales_list = queryset.values_list('online_sales', flat=True)
        online_price_list = queryset.values_list('online_price', flat=True)
        calc_dict = dict(
            business_calc=Business.objects.count(),
            store_calc=Store.objects.count(),
            product_calc=Product.objects.count(),
            retail_sales_calc=math.fsum(retail_sales_list),
            retail_price_calc=math.fsum(retail_price_list),
            project_sales_calc=math.fsum(project_sales_list),
            project_price_calc=math.fsum(project_price_list),
            wholesale_sales_calc=math.fsum(wholesale_sales_list),
            wholesale_price_calc=math.fsum(wholesale_price_list),
            online_sales_calc=math.fsum(online_sales_list),
            online_price_calc=math.fsum(online_price_list),
        )
        data["calc"] = calc_dict
        return render(request, 'hx/sales_record.html', {"data": data})
