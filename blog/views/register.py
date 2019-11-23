#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/11/19 0019 10:12
from django.shortcuts import render,redirect,HttpResponse,render_to_response
from api.models import User
from django.http import JsonResponse
from blog import forms,models
def index(request):
    user_obj = request.session.get('user_avatar')
    user = request.session.get('user_name')
    # user_id1 = request.session.get('user_id')
    # # 使用user_id去数据库中找到对应的user信息
    # userobj = User.objects.filter(id=user_id1)
    article_list = models.Article.objects.all()
    if user:
        return render(request, 'blog_index.html', {"article_list":article_list,"user": user,'user_obj':user_obj})



def register(request):
    user_obj = request.session.get('user_avatar')
    user = request.session.get('user_name')
    form_obj = forms.RegForm()
    ret = {"status": 0, "msg": ""}
    if request.method == "POST":
        form_obj = forms.RegForm(request.POST)
        print(form_obj)
        # 让form帮我们做校验
        if form_obj.is_valid():
            print(form_obj.cleaned_data)
            form_obj.cleaned_data.pop("re_password")
            avatar_img = request.FILES.get("avatar")
            print(avatar_img)
            if avatar_img:
                User.objects.create(**form_obj.cleaned_data, avatar=avatar_img)
                ret["msg"] = "/api/api_userinfo/"
                return JsonResponse(ret)
            else:
                User.objects.create(**form_obj.cleaned_data)
                ret["msg"] = "/api/api_userinfo/"
                return JsonResponse(ret)
        else:
            print(form_obj.errors)
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            return JsonResponse(ret)
    return render(request,'register.html',{'form_obj':form_obj,'user':user,'user_obj':user_obj})

def check_username_exist(request):
    ret = {"status": 0, "msg": ""}
    username = request.GET.get("username")
    print(username)
    is_exist = User.objects.filter(username=username)
    if is_exist:
        ret["status"] = 1
        ret["msg"] = "用户名已被注册！"
    return JsonResponse(ret)

def check_email_exist(request):
    ret ={"status":0,"msg":""}
    email = request.GET.get("email")
    is_exist = User.objects.filter(email=email)
    if is_exist:
        ret["status"] = 1
        ret["msg"] = "邮箱已被注册！"
    return JsonResponse(ret)









