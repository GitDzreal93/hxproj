# -*- coding:utf-8 -*-

from  django import forms


class SupplyDetailUploadForm(forms.Form):
    # name = forms.CharField(max_length=20,min_length=3,required=True,label='名称:')
    supply_file = forms.FileField(label='上传供货明细文件:')


