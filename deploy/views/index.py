#!/usr/bin/env python  
# _#_ coding:utf-8 _*_
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from api import models
from utils.check_login import check_login,require_login
@check_login
def index(request):
    user_id1 = request.session.get('user_id')
    # 使用user_id去数据库中找到对应的user信息
    userobj = models.User.objects.filter(id=user_id1)
    if userobj:
        return render(request, 'index.html', {"user": userobj[0]})
    else:
        return render(request, 'index.html', {'user', '匿名用户'})
def layout(request):
    user_id1 = request.session.get('user_id')
    # 使用user_id去数据库中找到对应的user信息
    userobj = models.User.objects.filter(id=user_id1)
    if userobj:
        return render(request, 'layout.html', {"user": userobj[0]})
    else:
        return render(request, 'layout.html', {'user', '匿名用户'})


#基于session校验
# 设置session
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.User.objects.filter(username=username, password=password)
        # 从URL里面取到 next 参数
        next_url = request.GET.get("next")

        if user:
            # 登陆成功
            # 告诉浏览器保存一个键值对

            if next_url:
                rep = redirect(next_url)  # 得到一个响应对象
            else:
                rep = redirect("/index/")  # 得到一个响应对象
            # 设置session
            request.session["is_login"] = "1"
            request.session['user_id'] = user[0].id
            request.session.set_expiry(70)  # 7秒钟之后失效
            return rep

    return render(request, "login.html")
#基于cookie的校验
# def login(request):
#     # print(request.get_full_path())  # 获取当前请求的路径和参数
#     # print(request.path_info)  # 取当前请求的路径
#     # print("-" * 120)
#
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = models.User.objects.filter(username=username, password=password)
#         # 从URL里面取到 next 参数
#         next_url = request.GET.get("next")
#
#         if user:
#             # 登陆成功
#             # 告诉浏览器保存一个键值对
#
#             if next_url:
#                 rep = redirect(next_url)  # 得到一个响应对象
#             else:
#                 rep = redirect("/index/")  # 得到一个响应对象
#
#             # rep.set_cookie("is_login", "1")
#             request.session['is_login'] = '1'
#             request.session['user_id'] = user[0].id
#             # 设置加盐的cookie
#             rep.set_signed_cookie("is_login", "1", salt="yang", max_age=10)  # 单位是秒
#             return rep
#
#     return render(request, "login.html")


def logout(request):
    #清楚session的记录
    request.session.delete()
    # return redirect("/login/")
    # 只删除session数据
    # request.session.delete()
    # 如何删除session数据和cookie
    request.session.flush()
    return redirect("/login/")