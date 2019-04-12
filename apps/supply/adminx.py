# -*- coding: utf-8 -*-

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import OrderRecord


class OrderRecordAdmin(object):
    list_display = ['id', 'business', 'product', 'order_date', 'order_num', 'count', 'price', 'total_price',
                    'create_time']
    search_fields = ['id', 'business', 'product', 'order_date', 'order_num', 'count', 'price', 'total_price']
    list_filter = ['id', 'business', 'product', 'order_date', 'order_num', 'count', 'price', 'total_price',
                   'create_time']
    model_icon = 'fa fa-address-book-o'



xadmin.site.register(OrderRecord, OrderRecordAdmin)
