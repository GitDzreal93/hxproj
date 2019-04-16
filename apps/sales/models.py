# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from apps.common.models import Store
from apps.common.models import Product


# Create your models here.


class SalesRecord(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="门店名称", help_text="门店名称")
    product = models.ForeignKey(Product, to_field="product_mod", on_delete=models.CASCADE, verbose_name="产品",
                                help_text="产品")
    upload_time = models.DateField(verbose_name="销售日期", help_text="销售日期")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间", help_text="创建时间")
    retail_sales = models.IntegerField(default=0,null=True, blank=True,verbose_name="零售销量", help_text="零售销量")
    retail_price = models.FloatField(default=0,null=True, blank=True,verbose_name="实际零售金额", help_text="实际零售金额")
    project_sales = models.IntegerField(default=0,null=True, blank=True, verbose_name="工程销量", help_text="工程销量")
    project_price = models.FloatField(default=0,null=True, blank=True, verbose_name="实际工程金额", help_text="实际工程金额")
    wholesale_sales = models.IntegerField(default=0,null=True, blank=True, verbose_name="批发销量", help_text="批发销量")
    wholesale_price = models.FloatField(default=0,null=True, blank=True, verbose_name="实际批发金额", help_text="实际批发金额")
    online_sales = models.IntegerField(default=0,null=True, blank=True, verbose_name="电商销量", help_text="电商销量")
    online = models.FloatField(default=0,null=True, blank=True, verbose_name="实际电商金额", help_text="实际电商金额")
    src = models.CharField(default="无",max_length=100,null=True, blank=True, verbose_name="数据来源", help_text="数据来源")
    extra = models.TextField(null=True, blank=True, verbose_name="拓展字段", help_text="拓展字段")

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "tb_sales_record"
        verbose_name = "销量记录"
        verbose_name_plural = verbose_name
