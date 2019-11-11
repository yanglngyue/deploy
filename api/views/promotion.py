#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/11/1 0001 16:34

from utils.check_login import check_login,require_login
from django.shortcuts import render,redirect,HttpResponse,render_to_response
from api import models
from utils.pager import PageInfo
#查
def Promotion_list(request):
    all_count = models.Promotion.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'api_promotion.html', 11)
    promotion_list = models.Promotion.objects.all()[page_info.start():page_info.end()]

    return render(request, 'api_promotion.html', {'promotion_list': promotion_list, 'page_info': page_info})
#增
def Promotion_add(request):
    error_msg = ""
    # 如果是POST请求,我就取到用户填写的数据
    if request.method == "POST":
        new_name = request.POST.get("promotion_name", None)
        new_name1 = request.POST.get("promotion_select", None)
        new_name2 = request.POST.get("promotion_extent", None)
        new_name3 = request.POST.get("promotion_info", None)
        new_name4 = request.POST.get("promotion_uptime", None)
        new_name5 = request.POST.get("promotion_ps", None)

        if new_name:
            # 通过ORM去数据库里新建一条记录
            models.Promotion.objects.create(name=new_name,select=new_name1,extent=new_name2,info=new_name3,uptime=new_name4,ps=new_name5)
            # 引导用户访问出版社列表页,查看是否添加成功  --> 跳转
            return redirect("/api/promotion_list/")
        else:
            error_msg = "名字不能为空!"
    # 用户第一次来,我给他返回一个用来填写的HTML页面
    return render(request, "api_promotion_add.html", {"error": error_msg})

#删
def Promotion_del(request):
    # 删除指定的数据
    # 1. 从GET请求的参数里面拿到将要删除的数据的ID值
    del_id = request.POST.get("nid", None)  # 字典取值,娶不到默认为None
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找到数据
        del_obj = models.Promotion.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面,跳转到出版社的列表页,查看删除是否成功
        # return redirect("/api/promotion_list/")
        return HttpResponse("ok")
    else:
        return HttpResponse("要删除的数据不存在!")
#改
def Promotion_edit(request):
    # 用户修改完版本库的名字,点击提交按钮,给我发来新的版本库名字
    if request.method == "POST":
        print(request.POST)
        # 取新出版社名字
        edit_id = request.POST.get("nid")
        new_name = request.POST.get("promotion_name", None)
        new_name1 = request.POST.get("promotion_select", None)
        new_name2 = request.POST.get("promotion_extent", None)
        new_name3 = request.POST.get("promotion_info", None)
        new_name4 = request.POST.get("promotion_uptime", None)
        new_name5 = request.POST.get("promotion_ps", None)
        # 更新出版社
        # 根据id取到编辑的是哪个出版社
        edit_Promotion = models.Promotion.objects.get(id=edit_id)
        edit_Promotion.name = new_name
        edit_Promotion.select = new_name1
        edit_Promotion.extent = new_name2
        edit_Promotion.info = new_name3
        edit_Promotion.uptime = new_name4
        edit_Promotion.ps = new_name5
        print(new_name)

        edit_Promotion.save()  # 把修改提交到数据库
        # 跳转出版社列表页,查看是否修改成功
        # return redirect("/api/promotion_list/")
        return HttpResponse('数据修改完成,请点击确认跳转至列表页')


    # 从GET请求的URL中取到id参数
    edit_id = request.GET.get("nid")
    if edit_id:
        # 获取到当前编辑的出版社对象
        Promotion_obj = models.Promotion.objects.get(id=edit_id)
        return render(request, "promotion_edit.html", {"Promotion": Promotion_obj})
    else:
        return HttpResponse("编辑的数据不存在!请点击确认跳转至列表页")