from datetime import datetime

# Create your models here.
from django.db import models
from apps.common.models import Business
from apps.common.models import Store
from apps.common.models import Product


class SupplyRecord(models.Model):
    business = models.ForeignKey(Business, to_field="business_code", on_delete=models.CASCADE, verbose_name="商家",
                                 help_text="商家")
    product = models.ForeignKey(Product, to_field="product_mod", on_delete=models.CASCADE, verbose_name="产品",
                                help_text="产品")
    order_date = models.DateField(verbose_name="发货日期", help_text="发货日期")
    order_id = models.CharField(max_length=20, verbose_name="订单号", help_text="订单号")
    count = models.IntegerField(verbose_name="要货数量", help_text="要货数量")
    price = models.FloatField(verbose_name="供价", help_text="供价")
    total_price = models.FloatField(verbose_name="供货总价", help_text="供货总价")
    remarks = models.TextField(default='', null=True, blank=True, verbose_name="备注", help_text="备注")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间", help_text="创建时间", null=True,
                                       blank=True)

    def __str__(self):
        return self.order_id

    class Meta:
        db_table = "tb_supply_record"
        verbose_name = "供货记录"
        verbose_name_plural = verbose_name
