#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/11/23 0023 10:01

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from cmdb.models import WeblogicPort

class PortForm(forms.Form):
    WeblogicPort = forms.ChoiceField(
        choices=WeblogicPort.objects.all().values_list("nid", "port"),
        label="服务应用端口号",
        initial='8002',
        widget=forms.widgets.Select
    )
    #
    # 重写父类的init方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["WeblogicPort"].widget.choices = WeblogicPort.objects.all().values_list("nid", "port")
    #     self.fields["mcpinterf"].widget.choices = models.WeblogicService.objects.all().values_list("nid",
    #                                                                                          "weblogicport__port"),