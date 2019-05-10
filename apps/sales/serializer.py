# -*- coding:utf-8 -*-
import json
import pandas as pd
from pprint import pprint
from dateutil.parser import parse

from rest_framework import serializers
from rest_framework.utils import html, model_meta, representation
from drf_writable_nested import WritableNestedModelSerializer

from pprint import pprint
from django.db.models import Q
from apps.common.models import Business, Store, Product
from apps.stock.models import Stock
from apps.sales.models import SalesRecord
from apps.common.serializer import BusinessSerializer
from apps.common.serializer import ProductSerializer
from apps.common.serializer import StoreSerializer
from utils.calc_stock import calc_stock


class SalesCalcSerializer(serializers.Serializer):
    bussiness_count = serializers.IntegerField(label="商家总数")
    store_count = serializers.IntegerField(label="门店总数")
    product_count = serializers.IntegerField(label="产品总数")
    retail_total_sales = serializers.IntegerField(label="零售总销量")
    retail_total_price = serializers.FloatField(label="实际零售总额")
    project_total_sales = serializers.IntegerField(label="工程总销量")
    project_total_price = serializers.FloatField(label="实际工程总额")
    wholesale_total_sales = serializers.IntegerField(label="批发总销量")
    wholesale_total_price = serializers.FloatField(label="实际批发总额")
    online_total_sales = serializers.IntegerField(label="电商总销量")
    online_total_price = serializers.FloatField(label="实际电商总额")


class SalesRecordSerializer(WritableNestedModelSerializer):
    business = BusinessSerializer()
    product = ProductSerializer()
    store = StoreSerializer()

    class Meta:
        model = SalesRecord
        fields = "__all__"
        depth = 1
