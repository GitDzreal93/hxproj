# -*- coding:utf-8 -*-
# 独立使用django的model
import sys
import os
import abc

import pandas as pd
from pprint import pprint

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hxproj.settings")
from hxproj import settings

from apps.common.serializer import UploadFileSerializer, BusinessSerializer, ProductSerializer,StoreSerializer
from apps.sales.serializer import SalesRecordSerializer
from apps.stock.serializer import StockNowSerializer
from apps.supply.serializer import SupplyRecordSerializer


class BaseFileParser(metaclass=abc.ABCMeta):
    def __init__(self, name=None, model_name=None, file_path=None, sheet_name=None, **kwargs):
        self._name = name
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.model_name = model_name
        self._data = self.read_file()

    def read_file(self):
        df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
        pprint(df)
        df.fillna("", inplace=True)
        data_lst = df.to_dict(orient='records')
        pprint(data_lst)
        return data_lst

    def get_data(self):
        return self._data

    @abc.abstractmethod
    def parse(self, input):
        pass

    @abc.abstractmethod
    def save_db(self, parse_data):
        pass


class SalesFileParser(BaseFileParser):
    def parse(self, input):
        output = []
        for input_item in input:
            # 格式化时间
            sales_date = input_item.get("时间")
            sales_date = sales_date.date()
            # 生成存储字典
            output_dict = dict(
                business=dict(
                    business_code=input_item.get("商家代码"),
                    business_name=input_item.get("商家名称"),
                ),
                store=dict(
                    store_code=input_item.get("门店代码"),
                    store_name=input_item.get("门店名称"),
                    business=dict(
                        business_code=input_item.get("商家代码"),
                        business_name=input_item.get("商家名称"),
                    )
                ),
                product=dict(
                    product_mod=input_item.get("型号"),
                ),
                sales_date=sales_date,
                retail_sales=input_item.get("零售销量"),
                retail_price=float(input_item.get("实际零售金额")),
                project_sales=input_item.get("工程销量"),
                project_price=float(input_item.get("实际工程金额")),
                wholesale_sales=input_item.get("批发销量"),
                wholesale_price=float(input_item.get("实际批发金额")),
                online_sales=input_item.get("电商销量"),
                online_price=float(input_item.get("实际电商金额")),
                data_src=input_item.get("数据来源"),
            )
            output.append(output_dict)
        return output

    def save_db(self, parse_data):
        for i in parse_data:
            sales_record_serializer = SalesRecordSerializer(data=i)
            sales_record_serializer.is_valid(raise_exception=True)
            sales_record_serializer.save()
            print("插入销量数据成功")


class SupplyFileParser(BaseFileParser):
    def parse(self, input):
        output = []
        for input_item in input:
            # 格式化时间
            order_date = input_item.get("发货日期")
            order_date = order_date.date()
            # 生成存储字典
            output_dict = dict(
                business=dict(
                    business_code=input_item.get("商家代码"),
                    business_name=input_item.get("商家名称")
                ),
                product=dict(
                    product_mod=input_item.get("型号")
                ),
                count=input_item.get("要货数量"),
                price=input_item.get("供价"),
                total_price=input_item.get("要货金额"),
                order_id=input_item.get("订单号"),
                order_date=order_date,
                remarks=input_item.get("备注")
            )
            output.append(output_dict)
        return output

    def save_db(self, parse_data):
        for i in parse_data:
            supply_record_serializer = SupplyRecordSerializer(data=i)
            supply_record_serializer.is_valid(raise_exception=True)
            supply_record_serializer.save()
            print("插入要货数据成功")


class InitFileParser(BaseFileParser):
    def parse(self, input):
        output = []
        for input_item in input:
            # 生成存储字典
            output_dict = dict(
                business=dict(
                    business_code=input_item.get("商家代码"),
                    business_name=input_item.get("商家名称")
                ),
                product=dict(
                    product_mod=input_item.get("机型")
                ),
                stock_count=input_item.get("数量"),
                remarks=input_item.get("备注"),
                is_init=True
            )
            output.append(output_dict)
        return output

    def save_db(self, parse_data):
        for i in parse_data:
            stock_record_serializer = StockNowSerializer(data=i)
            stock_record_serializer.is_valid(raise_exception=True)
            stock_record_serializer.save()
            print("插入初始数据成功")
