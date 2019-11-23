#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/11/19 0019 10:10

"""
BLOG 用到的form类
"""

from django import forms
from django.core.exceptions import ValidationError
from api import models
# 定义一个注册的form类
class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label="用户名",
        error_messages={
            "max_length": "用户名最长16位",
            "required": "用户名不能为空",
        },
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    password = forms.CharField(
        min_length=6,
        label="密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True,
        ),
        error_messages={
            "min_length": "密码至少要6位！",
            "required": "密码不能为空",
        }
    )

    re_password = forms.CharField(
        min_length=6,
        label="确认密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True,
        ),
        error_messages={
            "min_length": "确认密码至少要6位！",
            "required": "确认密码不能为空",
        }
    )

    email = forms.EmailField(
        label="邮箱",
        widget=forms.widgets.EmailInput(
            attrs={"class": "form-control"},

        ),
        error_messages={
            "invalid": "邮箱格式不正确！",
            "required": "邮箱不能为空",
        }
    )

    # 设置一个用户名的局部钩子，用以校验用户名是否已经被注册，提交时候提示
    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_exist = models.User.objects.filter(username=username)
        if is_exist:
            # 表示用户名已注册
            self.add_error("username", ValidationError("用户名已被注册，请尝试其他用户名"))
        else:
            return username

    # 设置一个邮箱的局部钩子，用以校验邮箱是否已经被注册，提交时候提示
    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_exist = models.User.objects.filter(email=email)
        if is_exist:
            self.add_error("email",ValidationError("邮箱已经被注册，请更换其他邮箱"))
        else:
            return email

    # 重写全局的钩子函数，对确认密码做校验
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致"))

        else:
            return self.cleaned_data
