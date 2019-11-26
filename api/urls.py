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

    url(r'^task_del/', task_test.task_del,name='task_del'),
    #任务发布初始化
    url(r'^mcp_task_work/', task_test.mcp_task_work,name='mcp_task_work'),
    url(r'^mcpinterf_task_work/', task_test.mcpinterf_task_work,name='mcpinterf_task_work'),
    url(r'^tomcat_task_work/', task_test.tomcat_task_work,name='tomcat_task_work'),
    url(r'^linux_task_work/', task_test.linux_task_work,name='linux_task_work'),
    url(r'^task_upload/', task_test.task_upload,name='task_upload'),
    #任务发布 部署
    url(r'^mcp_put_task/', task_test.mcp_put_task,name='mcp_put_task'),
    url(r'^mcpinterf_put_task/', task_test.mcpinterf_put_task,name='mcpinterf_put_task'),
    url(r'^tomcat_put_task/', task_test.tomcat_put_task,name='tomcat_put_task'),
    url(r'^linux_put_task/', task_test.linux_put_task,name='linux_put_task'),
    #任务发布主页，为了练习代码量，采用了重复写的笨方法，其实可以共用一套html
    url(r'^mcp_operate_index/', task_test.mcp_operate_index,name='mcpinterf_operate_index'),
    url(r'^mcpinterf_operate_index/', task_test.mcpinterf_operate_index,name='mcpinterf_operate_index'),
    url(r'^tomcat_operate_index/', task_test.tomcat_operate_index,name='tomcat_operate_index'),
    url(r'^linux_operate_index/', task_test.linux_operate_index,name='linux_operate_index'),
    #任务发布 重启
    url(r'^port_reboot_task/', task_test.port_reboot_task,name='port_reboot_task'),

    url(r'^linux_operate_task/', task_test.linux_operate_task,name='port_operate_task'),







]