# -*- coding:utf-8 -*-
from rest_framework import serializers
from django.db.models import Q
from apps.common.models import Business, Store, Product


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()

    class Meta:
        model = Store
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
