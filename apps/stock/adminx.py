# -*- coding: utf-8 -*-

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import Stock, StockHistory


class StockAdmin(object):
    list_display = ['business', 'product', 'stock_count', 'is_init', 'remarks', 'create_time', 'modify_time']
    search_fields = ['business', 'product', 'stock_count']
    list_filter = ['business', 'product', 'stock_count', 'create_time', 'modify_time']
    model_icon = 'fa fa-address-book-o'


class StockHistoryAdmin(object):
    list_display = ['business', 'product', 'stock_count', 'is_init', 'record_time', 'create_time']
    search_fields = ['business', 'product', 'stock_count']
    list_filter = ['business', 'product', 'stock_count', 'create_time']
    model_icon = 'fa fa-address-book-o'


xadmin.site.register(Stock, StockAdmin)
xadmin.site.register(StockHistory, StockHistoryAdmin)
