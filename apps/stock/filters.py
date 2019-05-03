# -*- coding:utf-8 -*-
import django_filters
from apps.common.models import *
from apps.stock.models import *


class StockNowFilter(django_filters.rest_framework.FilterSet):
    """
    过滤库存信息
    """
    business_code = django_filters.CharFilter(field_name='business_id')
    product_mod = django_filters.CharFilter(field_name='product_id')
    is_init = django_filters.BooleanFilter()
    stock_count = django_filters.RangeFilter()

    class Meta:
        model = Stock
        fields = ['business_code', 'product_mod', 'stock_count', 'is_init']


class StockHistoryFilter(django_filters.rest_framework.FilterSet):
    """
    过滤历史库存信息
    """
    business_code = django_filters.CharFilter(field_name='business_id')
    product_mod = django_filters.CharFilter(field_name='product_id')
    is_init = django_filters.BooleanFilter()
    record_time = django_filters.DateFromToRangeFilter()
    stock_count = django_filters.RangeFilter()

    class Meta:
        model = StockHistory
        fields = ['business_code', 'product_mod', 'is_init', 'record_time', 'stock_count']
