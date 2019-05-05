# -*- coding:utf-8 -*-
from pprint import pprint
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin

from django.db.models import Q
from apps.common.models import Business, Store, Product, UploadFile


class BusinessSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"


class StoreSerializer(UniqueFieldsMixin, WritableNestedModelSerializer):
    # business = BusinessSerializer()
    business = BusinessSerializer()

    class Meta:
        model = Store
        fields = "__all__"


class ProductSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = "__all__"
