# -*- coding:utf-8 -*-
import json

from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from pprint import pprint
from django.db.models import Q
from apps.common.models import Business, Store, Product
from apps.stock.models import Stock, StockHistory
from apps.common.serializer import BusinessSerializer
from apps.common.serializer import ProductSerializer
from apps.common.serializer import StoreSerializer


class StockNowSerializer(WritableNestedModelSerializer):
    business = BusinessSerializer()
    product = ProductSerializer()

    class Meta:
        model = Stock
        fields = "__all__"


class StockHistorySerializer(WritableNestedModelSerializer):
    business = BusinessSerializer()
    product = ProductSerializer()

    class Meta:
        model = StockHistory
        fields = "__all__"

# class Stock(models.Model):
#     business = models.ForeignKey(Business, to_field="business_code", on_delete=models.CASCADE, verbose_name="商家名称",
#                                  help_text="商家名称")
#     product = models.ForeignKey(Product, to_field="product_mod", on_delete=models.CASCADE, verbose_name="产品",
#                                 help_text="产品")
#     stock_count = models.IntegerField(verbose_name="库存数", help_text="库存数")
#     remarks = models.TextField(default='', null=True, blank=True, verbose_name="备注", help_text="备注")
#     is_init = models.BooleanField(default=False, verbose_name="初始数据", help_text="是否是初始导入的数据")
#     create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="创建时间", help_text="创建时间")
#     modify_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="更新时间", help_text="更新时间")
#
#     def __str__(self):
#         return self.business.business_name + '-' + str(self.stock_count)
#
#     class Meta:
#         db_table = "tb_stock"
#         verbose_name = "库存"
#         verbose_name_plural = verbose_name
