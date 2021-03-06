# -*- coding:utf-8 -*-
# 独立使用django的model
import sys
import os
import abc
import datetime

import pandas as pd
from dateutil.parser import parse
from pprint import pprint

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hxproj.settings")

import django

django.setup()
from hxproj import settings

# from apps.common.models import UploadFile,Business,Product,Store
# from apps.supply.models import SupplyRecord
# from apps.sales.models import SalesRecord
# from apps.stock.models import Stock
# from apps.supply.models import SupplyRecord

from apps.common.serializer import UploadFileSerializer,BusinessSerializer,ProductSerializer
from apps.supply.serializer import SupplyRecordSerializer
from apps.sales.serializer import SalesRecordSerializer
from apps.stock.serializer import StockHistorySerializer,StockNowSerializer
from apps.supply.serializer import SupplyRecordSerializer

# UPLOAD_DIR = os.path.join(settings.MEDIA_ROOT, 'upload')


class BaseFileParser(metaclass=abc.ABCMeta):
    def __init__(self, name=None, model_name=None, file_path=None, sheet_name=None, **kwargs):
        self._name = name
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.model_name = model_name
        self._data = self.read_file()

    def read_file(self):
        df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
        df.fillna("", inplace=True)
        data_lst = df.to_dict(orient='records')
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
            sales_date=input_item.get("时间")
            sales_date = sales_date.date()
            # 生成存储字典
            output_dict = dict(
                business = dict(
                    business_code=input_item.get("商家代码"),
                    business_name=input_item.get("商家名称"),
                ),
                store = dict(
                    store_code=input_item.get("门店代码"),
                    store_name=input_item.get("门店名称"),
                    business = dict(
                        business_code=input_item.get("商家代码"),
                        business_name=input_item.get("商家名称"),
                    )
                ),
                product = dict(
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
            order_date=input_item.get("发货日期")
            order_date = order_date.date()
            # 生成存储字典
            output_dict = dict(
                business = dict(
                    business_code=input_item.get("商家代码"),
                    business_name=input_item.get("商家名称")
                ),
                product = dict(
                    product_mod=input_item.get("型号")
                ),
                count = input_item.get("要货数量"),
                price = input_item.get("供价"),
                total_price = input_item.get("要货金额"),
                order_id = input_item.get("订单号"),
                order_date = order_date,
                remarks = input_item.get("备注")
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



if __name__ == '__main__':
    # file_path = 'media/upload/16_2019-05-06_进存销格式.xlsx'
    # media/upload/16_2019-05-06_进销存格式.xlsx
    UPLOAD_DIR = settings.UPLOAD_ROOT
    file_path = os.path.join(UPLOAD_DIR, '26_2019-05-09_进销存格式销售记录.xlsx')

    # sheet_name = "销售数据导入"
    # sales_parser = SalesFileParser(name='sales', file_path=file_path, sheet_name=sheet_name)
    # data_input = sales_parser.get_data()
    # parse_data = sales_parser.parse(data_input)
    # print(parse_data)
    # sales_parser.save_db(parse_data)

    # sheet_name = "发货数据导入"
    # supply_parser = SupplyFileParser(name='supply', file_path=file_path, sheet_name=sheet_name)
    # data_input = supply_parser.get_data()
    # parse_data = supply_parser.parse(data_input)
    # supply_parser.save_db(parse_data)

    sheet_name = "初期库存导入"
    init_parser = InitFileParser(name='init_stock', file_path=file_path, sheet_name=sheet_name)
    init_input_data = init_parser.get_data()
    init_parse_data = init_parser.parse(init_input_data)
    init_parser.save_db(init_parse_data)

# df = pd.read_excel(f, sheet_name="销售数据导入")
# df.fillna("", inplace=True)
# data_lst = df.to_dict(orient='records')
# for input_data in data_lst:
#     business_code = input_data.get("商家代码")
#     business_name = input_data.get("商家名称")
#     store_code = input_data.get("门店代码")
#     store_name = input_data.get("门店名称")
#     product_mod = input_data.get("型号")
#     sales_time = parse(input_data.get("时间")) if type(input_data.get("时间")) == int else input_data.get("时间")
#     retail_sales = input_data.get("零售销量")
#     retail_price = float(input_data.get("实际零售金额"))
#     project_sales = input_data.get("工程销量")
#     project_price = float(input_data.get("实际工程金额"))
#     wholesale_sales = input_data.get("批发销量")
#     wholesale_price = float(input_data.get("实际批发金额"))
#     online_sales = input_data.get("电商销量")
#     online_price = float(input_data.get("实际电商金额"))
#     data_src = input_data.get("数据来源")
#     # 假如没有商家信息的话，就插入商家信息
#     try:
#         Business.objects.get(business_code=business_code)
#     except Business.DoesNotExist:
#         Business(
#             business_code=business_code,
#             business_name=business_name
#         ).save()
#     # 假如没有门店信息的话，就插入门店信息
#     try:
#         Store.objects.get(store_code=store_code)
#     except Store.DoesNotExist:
#         Store(
#             business_id=business_code,
#             store_code=store_code,
#             store_name=store_name,
#         ).save()
#     # 假如没有产品型号信息的话，就插入产品
#     try:
#         Product.objects.get(product_mod=product_mod)
#     except Product.DoesNotExist:
#         Product(
#             product_mod=product_mod
#         ).save()
#     # 插入销售明细
#     SalesRecord(
#         business_id=business_code,
#         store_id=store_code,
#         product_id=product_mod,
#         sales_time=sales_time,
#         retail_sales=retail_sales,
#         retail_price=retail_price,
#         project_sales=project_sales,
#         project_price=project_price,
#         wholesale_sales=wholesale_sales,
#         wholesale_price=wholesale_price,
#         online_sales=online_sales,
#         online_price=online_price,
#         data_src=data_src,
#     ).save()
# queryset = list(SalesRecord.objects.all().values())
# return render(request, 'sales_upload.html', {"formlist": data_lst, "querydata": queryset})
