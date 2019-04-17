# -*- coding:utf-8 -*-
from __future__ import absolute_import
import json
from dateutil.parser import parse
import pandas as pd

from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from .forms import UploadSalesDetailForm
from apps.sales.models import SalesRecord
from apps.common.models import Business, Product, Store


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
                print("business_code", type(business_code))
                print("business_name", type(business_name))
                print("store_code", type(store_code))
                print("store_name", type(store_name))
                print("product_mod", type(product_mod))
                print("sales_time", type(sales_time))
                print(sales_time)
                print("retail_sales", type(retail_sales))
                print("retail_price", type(retail_price))
                print("project_sales", type(project_sales))
                print("project_price", type(project_price))
                print("wholesale_sales", type(wholesale_sales))
                print("wholesale_price", type(wholesale_price))
                print("online_sales", type(online_sales))
                print("online_price", type(online_price))
                print("data_src", type(data_src))
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
