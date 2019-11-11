#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/31 0031 17:34
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from utils.pager import PageInfo
from utils.check_login import check_login,require_login
from api.models import User
from cmdb import models
@check_login
def index(request):
    # # 去请求的cookie中找凭证
    # # tk = request.COOKIES.get('ticket')
    # tk = request.get_signed_cookie('ticket', salt='jjjjjj')
    # if not tk:
    #     return redirect('/login/')
    # else:
    user_id1 = request.session.get('user_id')
    # 使用user_id去数据库中找到对应的user信息
    userobj = User.objects.filter(id=user_id1)
    if userobj:
        return render(request, 'cmdb_index.html', {"user": userobj[0]})
    else:
        return render(request, 'cmdb_index.html', {'user', '匿名用户'})


@check_login
def CmdbInfo(request):
    all_count = models.CmdbInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'cmdb_cmdbinfo.html', 11)
    cmdb_list = models.CmdbInfo.objects.all()[page_info.start():page_info.end()]

    return render(request, 'cmdb_cmdbinfo.html', {'cmdb_list': cmdb_list, 'page_info': page_info})