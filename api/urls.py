#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/23 0023 9:12



from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from api.views import index,promotion,task_test
urlpatterns = [
    url(r'^index/', index.index,name='index'),
    url(r'^api_userinfo/', index.api_userinfo,name='api_userinfo'),
    url(r'^promotion_list/', promotion.Promotion_list,name='promotion_list'),
    url(r'^promotion_add/', promotion.Promotion_add,name='promotion_add'),
    url(r'^promotion_del/', promotion.Promotion_del,name='promotion_del'),
    url(r'^promotion_edit/', promotion.Promotion_edit,name='promotion_edit'),
    url(r'^task_index/', task_test.task_index,name='task_index'),
    url(r'^task_work/', task_test.task_work,name='task_work'),
    url(r'^task_upload/', task_test.task_upload,name='task_upload'),

    url(r'^put_task/', task_test.put_task,name='put_task'),
    url(r'^reboot_task/', task_test.reboot_task,name='reboot_task'),







]