from django.shortcuts import render
import pandas as pd

# Create your views here.
from django.http import HttpResponse
from celery_app.tasks import run_test_suit



def tasks(request):
    print('before run_test_suit')
    result = run_test_suit.delay('110')
    print(result)
    print('after run_test_suit')
    return HttpResponse("job is runing background~")

