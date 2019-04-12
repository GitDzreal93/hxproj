# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from apps.common.models import Store
from apps.common.models import Product


# Create your models here.


class SalesRecord(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="id", help_text="id")
    store = models.ForeignKey(Store, on_delete=models.PROTECT, verbose_name="门店名称", help_text="门店名称")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="产品", help_text="产品")
    upload_time = models.DateField(verbose_name="销售日期", help_text="销售日期")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间", help_text="创建时间")
    retail_sales = models.IntegerField(verbose_name="零售销量", help_text="零售销量")
    retail_price = models.FloatField(verbose_name="实际零售金额", help_text="实际零售金额")
    project_sales = models.IntegerField(verbose_name="工程销量", help_text="工程销量")
    project_price = models.FloatField(verbose_name="实际工程金额", help_text="实际工程金额")
    extra = models.TextField(verbose_name="拓展字段", help_text="拓展字段")

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "tb_sales_record"
        verbose_name = "销量记录"
        verbose_name_plural = verbose_name
