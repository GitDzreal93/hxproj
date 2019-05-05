# -*- coding:utf-8 -*-
from pprint import pprint
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin

from django.db.models import Q
from apps.common.models import Business, Store, Product


class BusinessSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"


# class StoreSerializer(serializers.ModelSerializer):
class StoreSerializer(UniqueFieldsMixin, WritableNestedModelSerializer):
    # business = BusinessSerializer()
    business = BusinessSerializer()

    class Meta:
        model = Store
        fields = "__all__"

        # def create(self, validated_data):
        #     business_data = validated_data.pop('business')
        #     business_existed = Business.objects.filter(**business_data)
        #     if not business_existed:
        #         business = Business.objects.create(**business_data)
        #         business_id = business.business_code
        #     else:
        #         business_id = business_existed.values('business_code')
        #     store = Store.objects.create(business_id=business_id,**validated_data)
        #     return store


class ProductSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
