# -*- coding: utf-8 -*-

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import SupplyRecord


class SupplyRecordAdmin(object):
    list_display = ['id', 'business', 'product', 'order_date', 'order_id', 'count', 'price', 'total_price', 'remarks',
                    'create_time']
    search_fields = ['id', 'order_date', 'order_id', 'count', 'price', 'total_price']
    list_filter = ['id', 'business', 'product', 'order_date', 'order_id', 'count', 'price', 'total_price',
                   'create_time']
    model_icon = 'fa fa-address-book-o'
    relfield_style = 'fk-ajax'


xadmin.site.register(SupplyRecord, SupplyRecordAdmin)
