# -*- coding: utf-8 -*-

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import SalesRecord


class SalesRecordAdmin(object):
    list_display = ['id', 'store', 'product', 'upload_time', 'create_time', 'retail_sales', 'retail_price',
                    'project_sales', 'project_price', 'extra']
    search_fields = ['id', 'store', 'product', 'retail_price', 'project_sales', 'project_price']
    list_filter = ['id', 'store', 'product', 'upload_time', 'create_time', 'retail_sales', 'retail_price',
                   'project_sales', 'project_price']
    model_icon = 'fa fa-address-book-o'



xadmin.site.register(SalesRecord, SalesRecordAdmin)
