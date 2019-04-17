# -*- coding:utf-8 -*-

from  django import forms


class UploadSupplyDetailForm(forms.Form):
    supply_file = forms.FileField(label='上传供货明细文件:')


