# Generated by Django 2.0.13 on 2019-04-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20190417_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesrecord',
            name='extra',
            field=models.TextField(blank=True, default='', help_text='拓展字段', null=True, verbose_name='拓展字段'),
        ),
    ]
