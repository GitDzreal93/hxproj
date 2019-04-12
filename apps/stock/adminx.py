# -*- coding: utf-8 -*-

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import Stock


class StockAdmin(object):
    list_display = ['business', 'store', 'product', 'stock_count', 'create_time', 'modify_time']
    search_fields = ['business', 'store', 'product', 'stock_count']
    list_filter = ['business', 'store', 'product', 'stock_count', 'create_time', 'modify_time']
    model_icon = 'fa fa-address-book-o'


xadmin.site.register(Stock, StockAdmin)
