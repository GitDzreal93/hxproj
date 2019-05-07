# -*- coding:utf-8 -*-
import os
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

from hxproj import settings
from apps.common.models import UploadFile, Business, Product, Store
from apps.supply.models import SupplyRecord
from apps.sales.models import SalesRecord
from apps.stock.models import Stock
from apps.supply.models import SupplyRecord
from apps.common.serializer import UploadFileSerializer, BusinessSerializer, ProductSerializer
from apps.supply.serializer import SupplyRecordSerializer
from apps.sales.serializer import SalesRecordSerializer
from apps.stock.serializer import StockHistorySerializer, StoreSerializer
from apps.supply.serializer import SupplyRecordSerializer
from utils.base_file_parser import SalesFileParser, SupplyFileParser


# from utils import


@receiver(post_save, sender=UploadFile)
def callback_calc_stock(sender, instance=None, created=False, **kwargs):
    print("开始读取文件，并存入库存--")
    UPLOAD_ROOT = settings.UPLOAD_ROOT
    INIT_SHEET = settings.INIT_SHEET
    SALES_SHEET = settings.SALES_SHEET
    SUPPLY_SHEET = settings.SUPPLY_SHEET
    file_path = instance.file_path
    # 存储销量记录的数据
    sales_parser = SalesFileParser(name='sales', file_path=file_path, sheet_name=SALES_SHEET)
    sales_input_data = sales_parser.get_data()
    sales_parse_data = sales_parser.parse(sales_input_data)
    sales_parser.save_db(sales_parse_data)
    # 存储供货记录的数据
    supply_parser = SupplyFileParser(name='supply', file_path=file_path, sheet_name=SUPPLY_SHEET)
    supply_input_data = supply_parser.get_data()
    suppy_parse_data = supply_input_data.parse(supply_input_data)
    supply_parser.save_db(suppy_parse_data)
    # 存储初始化记录的数据
    print(file_path)
    return None