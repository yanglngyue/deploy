#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/31 0031 17:34
from django.shortcuts import render, render_to_response,redirect,HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from utils.pager import PageInfo
from utils.check_login import check_login,require_login
from api.models import User,Partment
from cmdb import models

def index(request):
    # # 去请求的cookie中找凭证
    # # tk = request.COOKIES.get('ticket')
    # tk = request.get_signed_cookie('ticket', salt='jjjjjj')
    # if not tk:
    #     return redirect('/login/')
    # else:
    user_id1 = request.session.get('user_id')
    # # 使用user_id去数据库中找到对应的user信息
    # userobj = User.objects.filter(id=user_id1)
    user_obj = User.objects.filter(id=user_id1).values('avatar')
    user = request.session.get('user_name')
    if user:
        return render(request, 'cmdb_index.html', {"user": user,'user_obj':user_obj[0]['avatar']})
    # else:
    #     return render(request, 'cmdb_index.html', {'user', '匿名用户'})



def CmdbInfo(request):
    user_id1 = request.session.get('user_id')
    user_obj = User.objects.filter(id=user_id1).values('avatar')
    user = request.session.get('user_name')
    all_count = models.CmdbInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'cmdb_cmdbinfo.html', 11)
    cmdb_list = models.CmdbInfo.objects.all()[page_info.start():page_info.end()]

    return render(request, 'cmdb_cmdbinfo.html', {'cmdb_list': cmdb_list, 'page_info': page_info,'user':user,'user_obj':user_obj[0]['avatar']})

#删
def CmdbInfo_del(request):
    # 删除指定的数据
    # 1. 从GET请求的参数里面拿到将要删除的数据的ID值
    del_id = request.POST.get("nid", None)  # 字典取值,娶不到默认为None
    # 如果能取到id值
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找到数据
        del_obj = models.CmdbInfo.objects.get(id=del_id)
        # 删除
        del_obj.delete()
        # 返回删除后的页面,跳转到出版社的列表页,查看删除是否成功
        # return redirect("/api/promotion_list/")
        return HttpResponse("ok")
    else:
        return HttpResponse("要删除的数据不存在!")
#增
#form表单操作实现添加功能 此处为练习用
from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class CmdbForm(forms.Form):
    # username = forms.CharField(
    #     # 校验规则相关
    #     max_length=16,
    #     label="用户名",
    #     error_messages={
    #         "required": "该字段不能为空",
    #     },
    #     # widget控制的是生成html代码相关的
    #     widget=widgets.TextInput(attrs={"class": "form-control"})
    # )
    # password = forms.CharField(
    #     label="密码",
    #     min_length=6,
    #     max_length=10,
    #     widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
    #     error_messages={
    #         "min_length": "密码不能少于6位！",
    #         "max_length": "密码最长10位！",
    #         "required": "该字段不能为空",
    #     }
    # )
    #
    # re_pwd = forms.CharField(
    #         label="确认密码",
    #         min_length=6,
    #         max_length=10,
    #         widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
    #         error_messages={
    #             "min_length": "密码不能少于6位！",
    #             "max_length": "密码最长10位！",
    #             "required": "该字段不能为空",
    #         }
    #     )
    #
    # email = forms.EmailField(
    #     label="邮箱",
    #
    #     widget=widgets.EmailInput(attrs={"class": "form-control"}),
    #     error_messages={
    #         "required": "该字段不能为空",
    #     }
    # )
    # phone = forms.CharField(
    #     label="手机",
    #     # 自己定制校验规则
    #     validators=[
    #         RegexValidator(r'^[0-9]+$', '手机号必须是数字'),
    #         RegexValidator(r'^1[3-9][0-9]{9}$', '手机格式有误')
    #     ],
    #     widget=widgets.TextInput(attrs={"class": "form-control"}),
    #     error_messages={
    #         "required": "该字段不能为空",
    #     }
    # )

    hostname = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="主机名",
        error_messages={
            "required": "主机名不能为空",
        },
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

    network_ip = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="内网IP",
        error_messages={
            "required": "内网IP不能为空",
        },
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

    cpu = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="CPU",
        error_messages={
            "required": "CPU不能为空",
        },
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

    memory = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="内存",
        error_messages={
            "required": "内存不能为空",
        },
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

    disk = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="硬盘",
        error_messages={
            "required": "硬盘不能为空",
        },
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

    Partment = forms.ChoiceField(
        choices=Partment.objects.all().values_list("id", "name"),
        label="项目组",
        initial='1',
        widget=forms.widgets.Select
    )

    ps = forms.CharField(
        # 校验规则相关
        max_length=16,
        label="备注",
        error_messages={
            "required": "备注不能为空",
        },
        # widget控制的是生成html代码相关的
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )



    # 重写父类的init方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["Partment"].widget.choices = Partment.objects.all().values_list("id", "name")


    def clean_hostname(self):
        value = self.cleaned_data.get("hostname")
        if "金瓶梅" in value:
            raise ValidationError("不符合社会主义核心价值观！")
        return value

    # 重写父类的clean方法
    # def clean(self):
    #     # 此时 通过检验的字段的数据都保存在 self.cleaned_data
    #     pwd = self.cleaned_data.get("password")
    #     re_pwd = self.cleaned_data.get("re_pwd")
    #     if pwd != re_pwd:
    #         self.add_error("re_pwd", ValidationError("两次密码不一致"))
    #         raise ValidationError("两次密码不一致")
    #     return self.cleaned_data




def cmdb_add(request):
    form_obj = CmdbForm()
    user_id1 = request.session.get('user_id')
    user_obj = User.objects.filter(id=user_id1).values('avatar')
    user = request.session.get('user_name')
    if request.method == "POST":
        form_obj = CmdbForm(request.POST)
        print(form_obj)
        # 让form帮我们做校验
        if form_obj.is_valid():
            # 校验通过
            # 把数据存到数据库
            # 所有经过校验的数据都保存在 form_obj.cleaned_data
            platform = form_obj.cleaned_data.get("Partment")#根据name值获取对应的value值
            a = Partment.objects.get(id=platform)
            print(a)
            # models.CmdbInfo.objects.create(Partment=a)
            del form_obj.cleaned_data["Partment"]
            models.CmdbInfo.objects.create(**form_obj.cleaned_data,platform=a)
            return redirect('/cmdb/cmdbinfo/')

    return render(request,'cmdb_add.html',{"form_obj":form_obj,'user':user,'user_obj':user_obj[0]['avatar']})

#改  由于代码冗余该功能暂时不写，后续代码优化再重写
def cmdb_edit(request):
    pass
