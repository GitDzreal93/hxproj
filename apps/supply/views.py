# -*- coding:utf-8 -*-
from __future__ import absolute_import
import json
import pandas as pd

from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from .forms import UploadSupplyDetailForm
from apps.supply.models import OrderRecord
from apps.common.models import Business, Product, Store


class UploadSupplyDetailView(View):
    def get(self, request):
        return render(request, 'supply_upload.html')

    def post(self, request):
        '''导入供货信息'''
        supply_file = UploadSupplyDetailForm(request.POST, request.FILES)
        if supply_file.is_valid():
            f = request.FILES.get('supply_file')
            df = pd.read_excel(f, sheet_name="发货数据导入")
            df.fillna("", inplace=True)
            data_lst = df.to_dict(orient='records')
            for input_data in data_lst:
                business_code = input_data.get("商家代码")
                business_name = input_data.get("商家名称")
                order_date = input_data.get("发货日期")
                order_num = input_data.get("订单号")
                product_mod = input_data.get("型号")
                count = input_data.get("要货数量")
                price = input_data.get("供价")
                total_price = input_data.get("要货金额")
                remarks = input_data.get("备注")
                # 假如没有商家信息的话，就插入商家信息
                try:
                    Business.objects.get(business_code=business_code)
                except Business.DoesNotExist:
                    Business(
                        business_code=business_code,
                        business_name=business_name
                    ).save()
                # 假如没有产品型号信息的话，就插入产品
                try:
                    Product.objects.get(product_mod=product_mod)
                except Product.DoesNotExist:
                    Product(
                        product_mod=product_mod
                    ).save()
                # 插入供货明细
                OrderRecord(
                    business_id=business_code,
                    product_id=product_mod,
                    order_date=order_date,
                    order_num=order_num,
                    count=count,
                    price=price,
                    total_price=total_price,
                    remarks=remarks
                ).save()
            queryset = list(OrderRecord.objects.all().values())
            return render(request, 'supply_upload.html', {"formlist": data_lst, "querydata": queryset})


class SupplyRecordView(View):
    def get(self, request):
        queryset = OrderRecord.objects.all()
        data = {}
        data["title"] = dict(
            business_code='商家代码',
            business_name='商家名称',
            product_mod='产品型号',
            order_num='订单号',
            price='供价',
            count='要货数量',
            total_price='要货金额',
            remark='备注'
        )
        order_record_lst = []
        for order in queryset.values():
            # 获取商家信息
            business_code = order.get("business_id")
            business_query = Business.objects.filter(business_code=business_code).values('business_name')
            business_name = business_query[0].get("business_name")
            # 产品型号
            product_mod = order.get("product_id")
            order_dict = dict(
                business_code=business_code,
                business_name=business_name,
                product_mod=product_mod,
                order_num=order.get("order_num"),
                count=order.get("count"),
                price=order.get("price"),
                total_price=order.get("total_price"),
                remark=order.get("remark"),
            )
            order_record_lst.append(order_dict)
        data["order_lst"] = order_record_lst
        return render(request, 'hx/supply_record.html', {"data": data})
