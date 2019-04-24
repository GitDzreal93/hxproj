from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from celery_app.tasks import run_test_suit
from django.views.generic.base import View
from apps.common.models import Business, Product, Store
from apps.common.serializer import BusinessSerializer, StoreSerializer, ProductSerializer
from apps.common.filters import BusinessFilter, StoreFilter, ProductFilter
from rest_framework import viewsets, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend


class PageSet(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = "size"
    page_query_param = "page"
    max_page_size = 100


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
    search_fields = ('store_code', 'store_name')
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


class BusinessView(View):
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
