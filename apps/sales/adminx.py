# -*- coding: utf-8 -*-

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import SalesRecord


class SalesRecordAdmin(object):
    list_display = ['id', 'business', 'store', 'product', 'sales_time', 'create_time', 'retail_sales', 'retail_price',
                    'project_sales', 'project_price', 'wholesale_sales', 'wholesale_price', 'online_sales',
                    'online_price', 'data_src', 'extra']
    search_fields = ['id', 'data_src']
    list_filter = ['id', 'business', 'store', 'product', 'sales_time', 'create_time', 'retail_sales', 'retail_price',
                   'project_sales', 'project_price', 'wholesale_sales', 'wholesale_price', 'online_sales',
                   'online_price', 'data_src', ]
    model_icon = 'fa fa-address-book-o'
    relfield_style = 'fk-ajax'


xadmin.site.register(SalesRecord, SalesRecordAdmin)
