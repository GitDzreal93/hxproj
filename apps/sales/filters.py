# -*- coding:utf-8 -*-
import django_filters
from apps.common.models import *
from apps.sales.models import *


class SalesRecordFilter(django_filters.rest_framework.FilterSet):
    """
    过滤销售信息
    """
    business_code = django_filters.CharFilter(field_name='business_id')
    store_code = django_filters.CharFilter(field_name='store_id')
    product_mod = django_filters.CharFilter(field_name='product_id')
    sales_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = SalesRecord
        fields = ['business_code', 'store_code', 'product_mod', 'sales_date']
