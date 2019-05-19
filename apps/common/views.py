import os
import pandas as pd

# Create your views here.
from django.http import FileResponse,Http404
from django.shortcuts import render
from rest_framework import viewsets, filters, pagination
from rest_framework.response import Response
from collections import OrderedDict, namedtuple
from rest_framework.renderers import TemplateHTMLRenderer
from celery_app.tasks import run_test_suit
from django.views.generic.base import View
from django_filters.rest_framework import DjangoFilterBackend
from pprint import pprint

from hxproj import settings
from apps.common.models import Business, Product, Store, UploadFile
from apps.common.serializer import BusinessSerializer, StoreSerializer, ProductSerializer, UploadFileSerializer
from apps.common.filters import BusinessFilter, StoreFilter, ProductFilter


class DownLoadTemplateFile(View):
    def get(self, request):
        # print(dir(request.GET))
        # print(request.GET.get("file"))
        template_file = os.path.join(settings.FILE_TEMPLATE_ROOT, request.GET.get("file"))
        print(template_file)
        # file_end = template_file.split('.')[-1]
        if os.path.isfile(template_file):
            file = open(template_file, 'rb')
            print(file)
            response = FileResponse(file)
            print(response)
            response["Content-type"] = "application/vnd.ms-excel"
            # response["Content-type"] = "application/x-xls"
            response['Content-Disposition'] = 'attachment;filename="海信进存销-上传文件模版.xls"'
            return response


class PageSet(pagination.LimitOffsetPagination):
    default_limit = 10000
    limit_query_param = 'limit'
    offset_query_param = 'start'
    max_limit = None
    template = 'rest_framework/pagination/numbers.html'


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
    search_fields = ('business__business_code', 'store_code', 'store_name')
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


class StoreView(View):
    def get(self, request):
        return render(request, "hx/store.html")


class ProductView(View):
    def get(self, request):
        return render(request, "hx/product.html")


class UploadFileView(View):
    def get(self, request):
        return render(request, "hx/upload_file.html")
