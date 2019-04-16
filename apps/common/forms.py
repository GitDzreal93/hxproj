# -*- coding:utf-8 -*-

from  django import forms


class InitDataUploadForm(forms.Form):
    # name = forms.CharField(max_length=20,min_length=3,required=True,label='名称:')
    init_file = forms.FileField(label='上传初始化文件:')
