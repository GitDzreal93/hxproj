# _*_ encoding:utf-8 _*_
import datetime

from django.db import models
from apps.common.models import Business
from apps.common.models import Store
from apps.common.models import Product


# Create your models here.
class Stock(models.Model):
    business = models.ForeignKey(Business, to_field="business_code", related_name="stock_business",
                                 on_delete=models.CASCADE, verbose_name="商家名称",
                                 help_text="商家名称")
    product = models.ForeignKey(Product, to_field="product_mod", related_name="stock_product", on_delete=models.CASCADE,
                                verbose_name="产品",
                                help_text="产品")
    stock_count = models.IntegerField(verbose_name="库存数", help_text="库存数")
    remarks = models.TextField(default='', null=True, blank=True, verbose_name="备注", help_text="备注")
    is_init = models.BooleanField(default=False, verbose_name="初始数据", help_text="是否是初始导入的数据")
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="创建时间", help_text="创建时间", null=True,
                                       blank=True)
    modify_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="更新时间", help_text="更新时间", null=True,
                                       blank=True)

    def __str__(self):
        return self.business.business_name + '-' + str(self.stock_count)

    class Meta:
        db_table = "tb_stock"
        verbose_name = "库存"
        verbose_name_plural = verbose_name


class StockHistory(models.Model):
    business = models.ForeignKey(Business, to_field="business_code", on_delete=models.CASCADE, verbose_name="商家名称",
                                 help_text="商家名称")
    product = models.ForeignKey(Product, to_field="product_mod", on_delete=models.CASCADE, verbose_name="产品",
                                help_text="产品")
    stock_count = models.IntegerField(verbose_name="库存数", help_text="库存数")
    is_init = models.BooleanField(default=False, verbose_name="初始数据", help_text="是否是初始导入的数据")
    # 库存时间
    record_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="库存记录时间",
                                       help_text="库存记录时间")
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="创建时间", help_text="创建时间", null=True,
                                       blank=True)

    def __str__(self):
        return self.business.business_name + '-' + str(self.stock_count)

    class Meta:
        db_table = "tb_stock_history"
        verbose_name = "历史库存"
        verbose_name_plural = verbose_name
