# -*- coding: utf-8 -*-

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import Business
from .models import Store
from .models import Product
from apps.sales.models import SalesRecord
from apps.stock.models import Stock, StockHistory
from apps.supply.models import SupplyRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "海信进销存 Admin管理后台"
    site_footer = "海信进销存 Admin管理后台"
    menu_style = "accordion"
    apps_icons = {"appname": "icon"}

    def get_site_menu(self):
        return (
            {'title': '管理', 'menus': (
                {'title': '商家', 'url': self.get_model_url(Business, 'changelist')},
                {'title': '门店', 'url': self.get_model_url(Store, 'changelist')},
                {'title': '产品', 'url': self.get_model_url(Product, 'changelist')},
            )},
            {'title': '供货', 'menus': (
                {'title': '供货记录', 'url': self.get_model_url(SupplyRecord, 'changelist')},
            )},
            {'title': '销量', 'menus': (
                {'title': '销量记录', 'url': self.get_model_url(SalesRecord, 'changelist')},
            )},
            {'title': '库存', 'menus': (
                {'title': '商家当前库存', 'url': self.get_model_url(Stock, 'changelist')},
                {'title': '商家历史库存', 'url': self.get_model_url(StockHistory, 'changelist')},
            )},

        )


class BusinessAdmin(object):
    list_display = ['business_code', 'business_name', 'office', 'company_type', 'create_time', 'modify_time']
    search_fields = ['business_code', 'business_name', 'office', 'company_type']
    list_filter = ['business_code', 'business_name', 'office', 'company_type', 'create_time', 'modify_time']
    model_icon = 'fa fa-address-book-o'


class StoreAdmin(object):
    list_display = ['store_code', 'store_name', 'business', 'create_time', 'modify_time']
    search_fields = ['store_code', 'store_name']
    list_filter = ['store_code', 'store_name', 'business', 'create_time', 'modify_time']
    model_icon = 'fa fa-address-book-o'
    relfield_style = 'fk-ajax'


class ProductAdmin(object):
    list_display = ['product_name', 'product_mod', 'specifications', 'create_time', 'modify_time']
    search_fields = ['product_name', 'product_mod', 'specifications']
    list_filter = ['product_name', 'product_mod', 'specifications', 'create_time', 'modify_time']
    model_icon = 'fa fa-address-book-o'


xadmin.site.register(Business, BusinessAdmin)
xadmin.site.register(Store, StoreAdmin)
xadmin.site.register(Product, ProductAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
