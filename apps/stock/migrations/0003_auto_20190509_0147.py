# Generated by Django 2.0.13 on 2019-05-09 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20190506_0027'),
        ('stock', '0002_auto_20190505_0002'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together={('business', 'product')},
        ),
    ]