# -*- coding:utf-8 -*-
import django_filters
from apps.common.models import *
from apps.supply.models import *


class SupplyRecordFilter(django_filters.rest_framework.FilterSet):
    """
    过滤供货信息
    """
    business_code = django_filters.CharFilter(field_name='business_id')
    product_mod = django_filters.CharFilter(field_name='product_id')
    order_id = django_filters.CharFilter(field_name='order_id')
    order_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = SupplyRecord
        fields = ['business_code', 'product_mod', 'order_id', 'order_date']
