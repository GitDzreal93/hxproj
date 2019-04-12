# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from apps.common.models import Business
from apps.common.models import Store
from apps.common.models import Product


# Create your models here.
class Stock(models.Model):
    business = models.ForeignKey(Business, on_delete=models.PROTECT, verbose_name="商家名称", help_text="商家名称")
    store = models.ForeignKey(Store, on_delete=models.PROTECT, verbose_name="门店名称", help_text="门店名称")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="产品", help_text="产品")
    stock_count = models.IntegerField(verbose_name="库存数", help_text="库存数")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间", help_text="创建时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间", help_text="更新时间")

    def __str__(self):
        return self.business.business_name + '-' + str(self.stock_count)

    class Meta:
        db_table = "tb_stock"
        verbose_name = "库存"
        verbose_name_plural = verbose_name
