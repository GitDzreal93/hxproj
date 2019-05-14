from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, filters, pagination
from rest_framework.response import Response
from collections import OrderedDict, namedtuple
from rest_framework.renderers import TemplateHTMLRenderer
from celery_app.tasks import run_test_suit
from django.views.generic.base import View
from django_filters.rest_framework import DjangoFilterBackend
from pprint import pprint

from apps.common.models import Business, Product, Store, UploadFile
from apps.common.serializer import BusinessSerializer, StoreSerializer, ProductSerializer, UploadFileSerializer
from apps.common.filters import BusinessFilter, StoreFilter, ProductFilter




# class PageSet(pagination.PageNumberPagination):
#     page_size = 12
#     page_size_query_param = "size"
#     page_query_param = "page"
#     max_page_size = 300
#
#     def get_paginated_response(self, data):
#         return Response(OrderedDict([
#             ('count', self.page.paginator.count),
#             ('next', self.get_next_link()),
#             ('previous', self.get_previous_link()),
#             ('results', data)
#         ]))

class PageSet(pagination.LimitOffsetPagination):
    default_limit = 10000
    limit_query_param = 'limit'
    offset_query_param = 'start'
    max_limit = None
    template = 'rest_framework/pagination/numbers.html'
#     draw = 'draw'
#
#     def get_draw(self, request):
#         try:
#             return pagination._positive_int(
#                 request.query_params[self.draw],
#             )
#         except (KeyError, ValueError):
#             return 0
#
#     def get_paginated_response(self, data):
#         return Response(OrderedDict([
#             ('draw', self.draw),
#             ('recordsTotal', self.get_next_link()),
#             ('recordsFiltered', self.count),
#             ('data', data)
#         ]))


class IndexView(View):
    def get(self, request):
        return render(request, "hx/index.html")


class BusinessViewset(viewsets.ModelViewSet):
    '''
    商品信息 API
    '''
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    # 设置分页
    pagination_class = PageSet
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = BusinessFilter
    search_fields = ('business_name', 'business_code', 'office', 'company_type')
    ordering_fields = ('business_name', 'business_code', 'office', 'company_type')
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'hx/business.html'


class StoreViewset(viewsets.ModelViewSet):
    '''
    门店信息 API
    '''
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    # 设置分页
    pagination_class = PageSet
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = StoreFilter
    search_fields = ('business__business_code','store_code', 'store_name')
    ordering_fields = ('business_id', 'store_code', 'store_name')


class ProductViewset(viewsets.ModelViewSet):
    '''
    产品信息 API
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # 设置分页
    pagination_class = PageSet
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = ProductFilter
    search_fields = ('product_mod', 'product_name')
    ordering_fields = ('product_mod', 'product_name')


class UploadFileViewset(viewsets.ModelViewSet):
    '''
    上传文件 API
    '''
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer


class BusinessView(View):
    def get(self, request):
        return render(request, "hx/business.html")


class BusinessViewOld(View):
    def get(self, request):
        queryset = Business.objects.all()
        data = {}
        data["title"] = dict(
            business_code='商家代码',
            business_name='商家名称',
            office='办事处',
            company_type='公司类型'
        )
        business_lst = []
        for business in queryset.values():
            business_dict = dict(
                business_code=business.get("business_code"),
                business_name=business.get("business_name"),
                office=business.get("office"),
                company_type=business.get("company_type")
            )
            business_lst.append(business_dict)
        data["business_list"] = business_lst
        return render(request, "hx/business.html", {"data": data})


class StoreView(View):
    def get(self, request):
        queryset = Store.objects.all()
        data = {}
        data["title"] = dict(
            business_code='商家代码',
            business_name='所属商家',
            store_name='门店名称',
            store_code='门店代码',
        )
        store_lst = []
        for store in queryset.values():
            business_code = store.get("business_id")
            business_query = Business.objects.filter(business_code=business_code).values('business_name')
            business_name = business_query[0].get("business_name")
            store_dict = dict(
                business_name=business_name,
                business_code=business_code,
                store_name=store.get("store_name"),
                store_code=store.get("store_code"),
            )
            store_lst.append(store_dict)
        data["store_list"] = store_lst
        return render(request, "hx/store.html", {"data": data})


class ProductView(View):
    def get(self, request):
        queryset = Product.objects.all()
        data = {}
        data["title"] = dict(
            product_mod='产品型号',
            product_name='产品名称',
            specifications='产品规格',
        )
        product_lst = []
        for product in queryset.values():
            product_dict = dict(
                product_mod=product.get("product_mod"),
                product_name=product.get("product_name"),
                specifications=product.get("specifications"),
            )
            product_lst.append(product_dict)
        data["product_lst"] = product_lst
        print(data)
        return render(request, "hx/product.html", {"data": data})
