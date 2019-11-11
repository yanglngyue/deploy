#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/23 0023 9:14
from utils.check_login import check_login,require_login
from django.shortcuts import render,redirect,HttpResponse,render_to_response
from api import models
from utils.pager import PageInfo
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
    userobj = models.User.objects.filter(id=user_id1)
    if userobj:
        return render(request, 'api_index.html', {"user": userobj[0]})
    else:
        return render(request, 'api_index.html', {'user', '匿名用户'})
@check_login
def api_userinfo(request):

    all_count = models.User.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'api_userinfo.html', 11)
    user_list = models.User.objects.all()[page_info.start():page_info.end()]

    return render(request, 'api_userinfo.html', {'user_list': user_list, 'page_info': page_info})

@check_login
def custom(request):
    #获取所有数据条数
    # for i in range(100):
    #     name = "沙河"+str(i)
    #     models.Book.objects.create(title=name,publish_date="2019-10-15",price=100,memo=5,publisher_id=3)

    all_count = models.Book.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'custom.html', 11)
    user_list = models.Book.objects.all()[page_info.start():page_info.end()]

    return render(request, 'custom.html', {'user_list': user_list, 'page_info': page_info})

















