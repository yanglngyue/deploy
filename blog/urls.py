#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/31 0031 17:32

from django.conf.urls import url
from blog.views import register

urlpatterns = [
    url(r'^index/', register.index,name='index'),
    url(r'^register/', register.register,name='register'),
    url(r'^check_username_exist/', register.check_username_exist,name='check_username_exist'),
    url(r'^check_email_exist/', register.check_email_exist,name='check_email_exist'),





]
# + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)