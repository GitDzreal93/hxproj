# -*- coding:utf-8 -*-
import json

from rest_framework import serializers

from pprint import pprint
from django.db.models import Q
from apps.common.models import Business, Store, Product
from apps.supply.models import SupplyRecord
from apps.common.serializer import BusinessSerializer
from apps.common.serializer import ProductSerializer
from apps.common.serializer import StoreSerializer


class SupplyRecordSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()
    product = ProductSerializer()

    class Meta:
        model = SupplyRecord
        fields = "__all__"
