# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from apps.common.models import Store
from apps.common.models import Product
from apps.common.models import Business


# Create your models here.


class SalesRecord(models.Model):
    business = models.ForeignKey(Business, to_field="business_code", related_name="business", on_delete=models.CASCADE,
                                 verbose_name="商家代码",
                                 help_text="商家代码")
    store = models.ForeignKey(Store, to_field="store_code", related_name="store", on_delete=models.CASCADE,
                              verbose_name="门店代码",
                              help_text="门店代码")
    product = models.ForeignKey(Product, to_field="product_mod", related_name="product", on_delete=models.CASCADE,
                                verbose_name="产品型号",
                                help_text="产品型号")
    sales_time = models.DateField(verbose_name="销售日期", help_text="销售日期")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间", help_text="创建时间")
    retail_sales = models.IntegerField(default=0, null=True, blank=True, verbose_name="零售销量", help_text="零售销量")
    retail_price = models.FloatField(default=0, null=True, blank=True, verbose_name="实际零售金额", help_text="实际零售金额")
    project_sales = models.IntegerField(default=0, null=True, blank=True, verbose_name="工程销量", help_text="工程销量")
    project_price = models.FloatField(default=0, null=True, blank=True, verbose_name="实际工程金额", help_text="实际工程金额")
    wholesale_sales = models.IntegerField(default=0, null=True, blank=True, verbose_name="批发销量", help_text="批发销量")
    wholesale_price = models.FloatField(default=0, null=True, blank=True, verbose_name="实际批发金额", help_text="实际批发金额")
    online_sales = models.IntegerField(default=0, null=True, blank=True, verbose_name="电商销量", help_text="电商销量")
    online_price = models.FloatField(default=0, null=True, blank=True, verbose_name="实际电商金额", help_text="实际电商金额")
    data_src = models.CharField(default="", max_length=100, null=True, blank=True, verbose_name="数据来源",
                                help_text="数据来源")
    extra = models.TextField(default="", null=True, blank=True, verbose_name="拓展字段", help_text="拓展字段")

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "tb_sales_record"
        verbose_name = "销量记录"
        verbose_name_plural = verbose_name
