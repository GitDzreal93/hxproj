# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models


# Create your models here.


class Business(models.Model):
    business_code = models.CharField(unique=True, max_length=10, verbose_name="商家代码", help_text="商家代码")
    business_name = models.CharField(unique=True, max_length=100, verbose_name="商家名称", help_text="商家名称")
    office = models.CharField(max_length=50, verbose_name="办事处", help_text="办事处")
    type = models.CharField(max_length=50, verbose_name="公司分类", help_text="公司分类")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除", help_text="是否删除")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间", help_text="创建时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="修改时间", help_text="修改时间")

    def __str__(self):
        # return self.business_name + '({})'.format(self.business_code)
        return self.business_name

    class Meta:
        db_table = "tb_business"
        verbose_name = "商家"
        verbose_name_plural = verbose_name


class Store(models.Model):
    store_name = models.CharField(unique=True, max_length=100, verbose_name="门店名称", help_text="门店名称")
    business = models.ForeignKey(Business, on_delete=models.CASCADE, verbose_name="商家", help_text="商家")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除", help_text="是否删除")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间", help_text="创建时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间", help_text="更新时间")

    def __str__(self):
        return self.store_name

    class Meta:
        db_table = "tb_store"
        verbose_name = "门店"
        verbose_name_plural = verbose_name


class Product(models.Model):
    product_name = models.CharField(unique=True, max_length=100, verbose_name="产品名称", help_text="产品名称")
    product_mod = models.CharField(unique=True, max_length=100, verbose_name="产品型号", help_text="产品型号")
    specifications = models.TextField(verbose_name="规格", help_text="规格")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除", help_text="是否删除")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间", help_text="创建时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间", help_text="更新时间")


    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "tb_product"
        verbose_name = "产品"
        verbose_name_plural = verbose_name