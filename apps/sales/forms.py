# -*- coding:utf-8 -*-

from  django import forms


class UploadSalesDetailForm(forms.Form):
    sales_file = forms.FileField(label='上传供货明细文件:')


