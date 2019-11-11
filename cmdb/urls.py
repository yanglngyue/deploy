#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/31 0031 17:32

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from cmdb.views import cmdbinfo

urlpatterns = [
    url(r'^cmdbinfo/', cmdbinfo.CmdbInfo,name='CmdbInfo'),
    url(r'^index/', cmdbinfo.index,name='index'),




]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)