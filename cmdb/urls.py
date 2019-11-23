#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/31 0031 17:32

from django.conf.urls import url
from cmdb.views import cmdbinfo

urlpatterns = [
    url(r'^cmdbinfo/', cmdbinfo.CmdbInfo,name='CmdbInfo'),
    url(r'^index/', cmdbinfo.index,name='index'),
    url(r'^cmdb_add/', cmdbinfo.cmdb_add,name='cmdb_add'),
    url(r'^cmdb_del/', cmdbinfo.CmdbInfo_del,name='cmdb_del'),
    url(r'^cmdb_edit/', cmdbinfo.cmdb_edit,name='cmdb_edit'),




]