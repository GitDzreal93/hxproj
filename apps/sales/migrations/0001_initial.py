# Generated by Django 2.0.13 on 2019-04-14 19:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesRecord',
            fields=[
                ('id', models.IntegerField(auto_created=True, help_text='id', primary_key=True, serialize=False, verbose_name='id')),
                ('upload_time', models.DateField(help_text='销售日期', verbose_name='销售日期')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
                ('retail_sales', models.IntegerField(help_text='零售销量', verbose_name='零售销量')),
                ('retail_price', models.FloatField(help_text='实际零售金额', verbose_name='实际零售金额')),
                ('project_sales', models.IntegerField(help_text='工程销量', verbose_name='工程销量')),
                ('project_price', models.FloatField(help_text='实际工程金额', verbose_name='实际工程金额')),
                ('extra', models.TextField(help_text='拓展字段', verbose_name='拓展字段')),
                ('product', models.ForeignKey(help_text='产品', on_delete=django.db.models.deletion.CASCADE, to='common.Product', verbose_name='产品')),
                ('store', models.ForeignKey(help_text='门店名称', on_delete=django.db.models.deletion.CASCADE, to='common.Store', verbose_name='门店名称')),
            ],
            options={
                'verbose_name': '销量记录',
                'verbose_name_plural': '销量记录',
                'db_table': 'tb_sales_record',
            },
        ),
    ]
