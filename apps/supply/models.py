from datetime import datetime

# Create your models here.
from django.db import models
from apps.common.models import Business
from apps.common.models import Store
from apps.common.models import Product


class OrderRecord(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="id", help_text="id")
    business = models.ForeignKey(Business, on_delete=models.PROTECT, verbose_name="商家名称", help_text="商家名称")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="产品", help_text="产品")
    order_date = models.DateField(verbose_name="订单日期", help_text="订单日期")
    order_num = models.CharField(max_length=20, verbose_name="订单号", help_text="订单号")
    count = models.IntegerField(verbose_name="供货数量", help_text="供货数量")
    price = models.FloatField(verbose_name="供货单价", help_text="供供货单价")
    total_price = models.FloatField(verbose_name="供货总价", help_text="供货总价")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间", help_text="创建时间")

    def __str__(self):
        return self.order_num

    class Meta:
        db_table = "tb_order_record"
        verbose_name = "供货记录"
        verbose_name_plural = verbose_name
