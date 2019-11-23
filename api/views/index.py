#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/23 0023 9:14
from utils.check_login import check_login,require_login
from django.shortcuts import render,redirect,HttpResponse,render_to_response
from api import models
from utils.pager import PageInfo

def index(request):
    # # 去请求的cookie中找凭证
    # # tk = request.COOKIES.get('ticket')
    # tk = request.get_signed_cookie('ticket', salt='jjjjjj')
    # if not tk:
    #     return redirect('/login/')
    # else:
    user_id1 = request.session.get('user_id')
    user_obj = models.User.objects.filter(id=user_id1).values('avatar')
    # # 使用user_id去数据库中找到对应的user信息

    user = request.session.get('user_name')
    if user:
        return render(request, 'api_index.html', {"user": user,'user_obj':user_obj[0]['avatar']})

def api_userinfo(request):
    user_id1 = request.session.get('user_id')
    user_obj = models.User.objects.filter(id=user_id1).values('avatar')
    all_count = models.User.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'api_userinfo.html', 11)
    user_list = models.User.objects.all()[page_info.start():page_info.end()]
    user = request.session.get('user_name')
    return render(request, 'api_userinfo.html', {'user_list': user_list, 'page_info': page_info,'user':user,'user_obj':user_obj[0]['avatar']})

















