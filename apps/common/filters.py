# -*- coding:utf-8 -*-
import django_filters
from apps.common.models import *


class BusinessFilter(django_filters.rest_framework.FilterSet):
    """
    过滤商家信息
    """
    business_code = django_filters.CharFilter(field_name='business_code', lookup_expr='iexact')
    business_name = django_filters.CharFilter(field_name='business_name', lookup_expr='icontains')
    office = django_filters.CharFilter(field_name='office')
    company_type = django_filters.CharFilter(field_name='company_type')

    class Meta:
        model = Business
        fields = ['business_code', 'business_name', 'office', 'company_type']


class StoreFilter(django_filters.rest_framework.FilterSet):
    """
    过滤商家信息
    """

    business_id = django_filters.CharFilter(field_name='business_id', lookup_expr='iexact')
    store_name = django_filters.CharFilter(field_name='store_name', lookup_expr='icontains')
    store_code = django_filters.CharFilter(field_name='store_code', lookup_expr='iexact')

    class Meta:
        model = Store
        fields = ['business_id', 'store_name', 'store_code']


class ProductFilter(django_filters.rest_framework.FilterSet):
    """
    过滤产品信息
    """

    product_mod = django_filters.CharFilter(field_name='product_mod', lookup_expr='iexact')
    product_name = django_filters.CharFilter(field_name='product_name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['product_mod', 'product_name']
