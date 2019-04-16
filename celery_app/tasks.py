# -*- coding:utf-8 -*-
import datetime
import time
from celery import task
from celery.schedules import crontab
from django.db import transaction
from apps.stock.models import Stock, StockHistory


@task
def add(x, y):
    return x + y


@task
def run_test_suit(ts_id):
    print('jobs[ts_id=%s] running....' % ts_id)
    time.sleep(10.0)
    print('jobs[ts_id=%s] done' % ts_id)
    result = True
    return result


@task
def refresh_stock_history():
    now = datetime.datetime.now()
    start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
    # start = now - datetime.timedelta(seconds=)
    print(start)
    with transaction.atomic():
        queryset = Stock.objects.filter(create_time__gt=start)
        for row in queryset:
            StockHistory(
                business_id=row.business_id,
                product_id=row.product_id,
                stock_count=row.stock_count,
                record_time=row.modify_time,
                is_init=row.is_init,
            ).save()
