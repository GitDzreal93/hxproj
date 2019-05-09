# -*- coding:utf-8 -*-
import json
import pandas as pd
from pprint import pprint
from dateutil.parser import parse

from rest_framework import serializers
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

    def create(self, validated_data):
        business_id = validated_data["business"]["business_code"]
        product_id = validated_data["product"]["product_mod"]
        retail_sales = validated_data["retail_sales"]
        project_sales = validated_data["retail_sales"]
        wholesale_sales = validated_data["retail_sales"]
        online_sales = validated_data["retail_sales"]
        # 计算扣减库存表的产品库存
        now_stock = Stock.objects.filter(business_id=business_id, product_id=product_id)[0]
        now_stock.stock_count = now_stock.stock_count - (
        retail_sales + project_sales + wholesale_sales + online_sales)
        now_stock.save()
        return SalesRecord.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #更新库存数量
        instance.business_id = validated_data["business"]["business_code"]
        instance.product_id = validated_data["product"]["product_mod"]
        instance.retail_sales = validated_data["retail_sales"]
        instance.project_sales = validated_data["retail_sales"]
        instance.wholesale_sales = validated_data["retail_sales"]
        instance.online_sales = validated_data["retail_sales"]
        instance.retail_price = validated_data["retail_price"]
        instance.project_price = validated_data["project_price"]
        instance.wholesale_price = validated_data["wholesale_price"]
        instance.online_price = validated_data["online_price"]
        # 计算扣减库存表的产品库存
        now_stock = Stock.objects.filter(business_id=instance.business_id, product_id=instance.product_id)[0]
        now_stock.stock_count = now_stock.stock_count - (
            instance.retail_sales + instance.project_sales + instance.wholesale_sales + instance.online_sales)
        now_stock.save()
        instance.save()
        return instance
