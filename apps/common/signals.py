# -*- coding:utf-8 -*-
import pandas as pd

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db.backends.signals import connection_created
from django.db.models.signals import pre_migrate, post_migrate
from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception
from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate
from django.test.signals import setting_changed
from django.test.signals import template_rendered
from django.db.backends.signals import connection_created

from apps.common.models import UploadFile,Business,Product,Store
from apps.supply.models import SupplyRecord
from apps.sales.models import SalesRecord
from apps.stock.models import Stock
from apps.supply.models import SupplyRecord
# from utils import


@receiver(post_save,sender=UploadFile)
def callback_calc_stock(sender, instance=None, created=False, **kwargs):
    print("开始读取文件，并存入库存--")
    file_path = instance.file_path
    sheet_names = []


    print(file_path)
    return None


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

# df = pd.read_excel(f, sheet_name="发货数据导入")
# df.fillna("", inplace=True)
# data_lst = df.to_dict(orient='records')
# for input_data in data_lst:
#     business_code = input_data.get("商家代码")
#     business_name = input_data.get("商家名称")
#     order_date = input_data.get("发货日期")
#     order_id = input_data.get("订单号")
#     product_mod = input_data.get("型号")
#     count = input_data.get("要货数量")
#     price = input_data.get("供价")
#     total_price = input_data.get("要货金额")
#     remarks = input_data.get("备注")
#     # 假如没有商家信息的话，就插入商家信息
#     try:
#         Business.objects.get(business_code=business_code)
#     except Business.DoesNotExist:
#         Business(
#             business_code=business_code,
#             business_name=business_name
#         ).save()
#     # 假如没有产品型号信息的话，就插入产品
#     try:
#         Product.objects.get(product_mod=product_mod)
#     except Product.DoesNotExist:
#         Product(
#             product_mod=product_mod
#         ).save()
#     # 插入供货明细
#     SupplyRecord(
#         business_id=business_code,
#         product_id=product_mod,
#         order_date=order_date,
#         order_id=order_id,
#         count=count,
#         price=price,
#         total_price=total_price,
#         remarks=remarks
#     ).save()
# queryset = list(SupplyRecord.objects.all().values())
# return render(request, 'supply_upload.html', {"formlist": data_lst, "querydata": queryset})

    # df = pd.read_excel(f, sheet_name="初期库存导入")
    # df.fillna("", inplace=True)
    # data_lst = df.to_dict(orient='records')
    # input_lst = data_lst
    # for input_data in input_lst:
    #     business_info = Business(business_name=input_data.get("商家名称"), business_code=input_data.get("商家代码"))
    #     product_info = Product(product_mod=input_data.get("机型"))
    #     stock_info = Stock(business_id=input_data.get("商家代码"), product_id=input_data.get("机型"),
    #                        stock_count=input_data.get("数量"), remarks=input_data.get("备注"), is_init=True)
    #     # 插入商品表
    #     try:
    #         business_info.save()
    #     except Exception:
    #         return render(request, 'init_upload.html',
    #                       {"st": "failed", "errno": 1062, "errmsg": '插入数据库失败', "data": {}})
    #     # 插入产品表
    #     try:
    #         product_info.save()
    #     except Exception:
    #         return render(request, 'init_upload.html',
    #                       {"st": "fail", "errno": 1062, "errmsg": '插入数据库失败', "data": {}})
    #     # 插入库存表（初始）
    #     try:
    #         if not Stock.objects.filter(business_id=input_data.get("商家代码")):
    #             # 库存表的商家信息不能重复
    #             stock_info.save()
    #     except:
    #         return render(request, 'init_upload.html',
    #                       {"st": "fail", "errno": 1062, "errmsg": '插入数据库失败', "data": {}})
    # output_lst = Stock.objects.all().values()
    # return render(request, 'init_upload.html',
    #               {"err": "suceess", "errno": 0, "errmsg": '', "file_table": input_lst, "db_table": output_lst})