#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/31 0031 13:14
from functools import wraps
from django.shortcuts import redirect,render
from api import models
# 说明：这个装饰器的作用，就是在每个视图函数被调用时，都验证下有没法有登录，
# 如果有过登录，则可以执行新的视图函数，
# 否则没有登录则自动跳转到登录页面。
#session
def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.session.get("is_login")
        # 1. 获取cookie中的随机字符串
        # 2. 根据随机字符串去数据库取 session_data --> 解密 --> 反序列化成字典
        # 3. 在字典里面 根据 is_login 取具体的数据
        if ret == "1":
            # 已经登陆过的 继续执行
            return func(request, *args, **kwargs)
        # 没有登录过的 跳转到登录页面
        else:
            # 获取当前访问的URL
            next_url = request.path_info
            print(next_url)
            return redirect("/login/?next={}".format(next_url))
    return inner
#cookie
def require_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.get_signed_cookie("is_login", default="0", salt="yang")
        if ret == "1":
            # 已经登陆过的 继续执行
            return func(request, *args, **kwargs)
        # 没有登录过的 跳转到登录页面
        else:
            # 获取当前访问的URL
            next_url = request.path_info
            print(next_url)
            return redirect("/login/?next={}".format(next_url))
    return inner