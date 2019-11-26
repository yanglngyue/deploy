#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/11/1 0001 16:34
import os,django
from cmdb.forms import PortForm
from django.http import JsonResponse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deploy.settings")# project_name 项目名称
django.setup()

from utils.check_login import check_login,require_login
from django.shortcuts import render,redirect,HttpResponse
from api.models import User
from cmdb import models
from utils.pager import PageInfo
from fabric.api import *
import time
from django.core.files.storage import FileSystemStorage
ctime = "`date +%Y%m%d_%H%M%S`"
date_time= "`date +%Y%m%d`"
env.user = 'super'
# env.hosts = ['10.10.68.149']
# env.password = 'super123'
# env.host_string = '10.10.68.149'
# env.host_string = models.CmdbInfo.objects.values('network_ip')
env.key_filename = 'D:\Python\deploy\media\id_rsa'

def task_index(request):
    user_id1 = request.session.get('user_id')
    user_obj = User.objects.filter(id=user_id1).values('avatar')
    user = request.session.get('user_name')
    all_count = models.CmdbInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'task_push.html', 11)
    ip_list = models.CmdbInfo.objects.all()[page_info.start():page_info.end()]
    return render(request,'task_push.html',{'ip_list':ip_list,'page_info':page_info,'user':user,'user_obj':user_obj[0]['avatar']})


def mcp_operate_index(request):
    user_id1 = request.session.get('user_id')
    user_obj = User.objects.filter(id=user_id1).values('avatar')
    user = request.session.get('user_name')
    all_count = models.CmdbInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'mcp_operate.html', 11)
    ip_list = models.CmdbInfo.objects.all()[page_info.start():page_info.end()]
    return render(request,'mcp_operate.html',{'ip_list':ip_list,'page_info':page_info,'user':user,'user_obj':user_obj[0]['avatar']})
def mcpinterf_operate_index(request):
    user_id1 = request.session.get('user_id')
    user_obj = User.objects.filter(id=user_id1).values('avatar')
    user = request.session.get('user_name')
    all_count = models.CmdbInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'mcpinterf_operate.html', 11)
    ip_list = models.CmdbInfo.objects.all()[page_info.start():page_info.end()]
    return render(request,'mcpinterf_operate.html',{'ip_list':ip_list,'page_info':page_info,'user':user,'user_obj':user_obj[0]['avatar']})
def tomcat_operate_index(request):
    user_id1 = request.session.get('user_id')
    user_obj = User.objects.filter(id=user_id1).values('avatar')
    user = request.session.get('user_name')
    all_count = models.CmdbInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'tomcat_operate.html', 11)
    ip_list = models.CmdbInfo.objects.all()[page_info.start():page_info.end()]
    return render(request,'tomcat_operate.html',{'ip_list':ip_list,'page_info':page_info,'user':user,'user_obj':user_obj[0]['avatar']})
def linux_operate_index(request):
    user_id1 = request.session.get('user_id')
    user_obj = User.objects.filter(id=user_id1).values('avatar')
    user = request.session.get('user_name')
    all_count = models.CmdbInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'linux_operate.html', 11)
    ip_list = models.CmdbInfo.objects.all()[page_info.start():page_info.end()]
    return render(request,'linux_operate.html',{'ip_list':ip_list,'page_info':page_info,'user':user,'user_obj':user_obj[0]['avatar']})

def task_del(request):
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

def mcp_task_work(request):
    """
    请先在所有服务器创建/deploy文件夹,项目包路径/backup,/initconfig,停止脚本及启动脚本
    1、拷贝119上面的mcp.war到227本地
    2、227上面的mcp.war拷贝到149上面的/deploy下
    :return:
    """
    edit_id = request.POST.get("nid")
    print(edit_id)
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    print(env.host_string)
    # scp = "scp super@10.10.1.119:/home/samba/移动理赔平台V5050提测资料/interfaceUseServer.csv ./"
    # scp_put = "scp ./* %s@%s:/deploy/%s"%(env.user,env.host_string,date_time)
    # run('rm -rf /deploy/*;mkdir -p /deploy/`date +%Y%m%d`')
    # mkcd = 'function __mkcd(){ if [ $# == 1 ]; then mkdir $1; cd $1; unset -f __mkcd; elif [ $# == 2 ]; then mkdir $1 $2; cd $2; unset -f __mkcd; fi }; __mkcd'
    # local('%s /home/linux/apphome/%s;%s;%s'%(mkcd,ctime,scp,scp_put))
         #"with"的作用是让后面的表达式的语句继承当前状态，实现"cd /root/ && ls -l'的效果
    return HttpResponse('%s:mcp环境初始化完毕！'%(env.host_string))

def mcpinterf_task_work(request):
    """
    请先在所有服务器创建/deploy文件夹,项目包路径/backup,/initconfig,停止脚本及启动脚本
    1、拷贝119上面的mcp.war到227本地
    2、227上面的mcp.war拷贝到149上面的/deploy下
    :return:
    """
    edit_id = request.POST.get("nid")
    print(edit_id)
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    print(env.host_string)
    # scp = "scp super@10.10.1.119:/home/samba/移动理赔平台V5050提测资料/interfaceUseServer.csv ./"
    # scp_put = "scp ./* %s@%s:/deploy/%s"%(env.user,env.host_string,date_time)
    # run('rm -rf /deploy/*;mkdir -p /deploy/`date +%Y%m%d`')
    # mkcd = 'function __mkcd(){ if [ $# == 1 ]; then mkdir $1; cd $1; unset -f __mkcd; elif [ $# == 2 ]; then mkdir $1 $2; cd $2; unset -f __mkcd; fi }; __mkcd'
    # local('%s /home/linux/apphome/%s;%s;%s'%(mkcd,ctime,scp,scp_put))
         #"with"的作用是让后面的表达式的语句继承当前状态，实现"cd /root/ && ls -l'的效果
    return HttpResponse('%s:mcpinterf环境初始化完毕！'%(env.host_string))

def tomcat_task_work(request):
    """
    请先在所有服务器创建/deploy文件夹,项目包路径/backup,/initconfig,停止脚本及启动脚本
    1、拷贝119上面的mcp.war到227本地
    2、227上面的mcp.war拷贝到149上面的/deploy下
    :return:
    """
    edit_id = request.POST.get("nid")
    print(edit_id)
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    print(env.host_string)
    # scp = "scp super@10.10.1.119:/home/samba/移动理赔平台V5050提测资料/interfaceUseServer.csv ./"
    # scp_put = "scp ./* %s@%s:/deploy/%s"%(env.user,env.host_string,date_time)
    # run('rm -rf /deploy/*;mkdir -p /deploy/`date +%Y%m%d`')
    # mkcd = 'function __mkcd(){ if [ $# == 1 ]; then mkdir $1; cd $1; unset -f __mkcd; elif [ $# == 2 ]; then mkdir $1 $2; cd $2; unset -f __mkcd; fi }; __mkcd'
    # local('%s /home/linux/apphome/%s;%s;%s'%(mkcd,ctime,scp,scp_put))
         #"with"的作用是让后面的表达式的语句继承当前状态，实现"cd /root/ && ls -l'的效果
    return HttpResponse('%s:tomcat环境初始化完毕！'%(env.host_string))


def linux_task_work(request):
    """
    请先在所有服务器创建/deploy文件夹,项目包路径/backup,/initconfig,停止脚本及启动脚本
    1、拷贝119上面的mcp.war到227本地
    2、227上面的mcp.war拷贝到149上面的/deploy下
    :return:
    """
    edit_id = request.POST.get("nid")
    print(edit_id)
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    print(env.host_string)
    # scp = "scp super@10.10.1.119:/home/samba/移动理赔平台V5050提测资料/interfaceUseServer.csv ./"
    # scp_put = "scp ./* %s@%s:/deploy/%s"%(env.user,env.host_string,date_time)
    # run('rm -rf /deploy/*;mkdir -p /deploy/`date +%Y%m%d`')
    # mkcd = 'function __mkcd(){ if [ $# == 1 ]; then mkdir $1; cd $1; unset -f __mkcd; elif [ $# == 2 ]; then mkdir $1 $2; cd $2; unset -f __mkcd; fi }; __mkcd'
    # local('%s /home/linux/apphome/%s;%s;%s'%(mkcd,ctime,scp,scp_put))
         #"with"的作用是让后面的表达式的语句继承当前状态，实现"cd /root/ && ls -l'的效果
    return HttpResponse('%s:linux环境初始化完毕！'%(env.host_string))

def mcp_put_task(request):
    """
    1、备份149上面的mcp，前提新建当天的文件夹目录$(date -d "today" +"%Y%m%d_%H%M%S")
    2、将从227上传的mcp拷贝至项目发布目录，解压war包并替换主要配置文件
    :return:
    """

    edit_id = request.GET.get("nid")
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    print(env.host_string)
    domains =models.CmdbInfo.objects.get(id=edit_id).domains
    name_war = models.CmdbInfo.objects.get(id=edit_id).name_war
    # run('cp -rf %s/mcp %s/backup/%s'%(name_war,name_war,ctime))
    # run('rm -rf %s/mcp/*'%(name_war))
    # run('cp -rf /deploy/%s/mcp.war %s/mcp/'%(date_time,name_war))
    # time.sleep(5)
    # with cd('%s/mcp'%(name_war)):
    #     run('jar -xvf mcp.war')
    #     run('cp -rf %s/initconfig/* %s/mcp/WEB-INF/classes/'%(name_war,name_war))

    return HttpResponse('%smcp部署完毕！'%(env.host_string))
# def change_paper(chage_papername,chage_path):
#     cp = "cp -rf %s %s"%(chage_papername,chage_path)
#     with cd('/home/middleware/apphome/mcp/WEB-INF/classes/'):
#         run(cp)


def mcpinterf_put_task(request):
    """
    1、备份149上面的mcp，前提新建当天的文件夹目录$(date -d "today" +"%Y%m%d_%H%M%S")
    2、将从227上传的mcp拷贝至项目发布目录，解压war包并替换主要配置文件
    :return:
    """

    edit_id = request.GET.get("nid")
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    domains =models.CmdbInfo.objects.get(id=edit_id).domains
    name_war = models.CmdbInfo.objects.get(id=edit_id).name_war
    # run('cp -rf %s/mcp %s/backup/%s'%(name_war,name_war,ctime))
    # run('rm -rf %s/mcp/*'%(name_war))
    # run('cp -rf /deploy/%s/mcp.war %s/mcp/'%(date_time,name_war))
    # time.sleep(5)
    # with cd('%s/mcp'%(name_war)):
    #     run('jar -xvf mcp.war')
    #     run('cp -rf %s/initconfig/* %s/mcp/WEB-INF/classes/'%(name_war,name_war))

    return HttpResponse('%smcpinterf部署完毕！'%(env.host_string))



def tomcat_put_task(request):
    """
    1、备份149上面的mcp，前提新建当天的文件夹目录$(date -d "today" +"%Y%m%d_%H%M%S")
    2、将从227上传的mcp拷贝至项目发布目录，解压war包并替换主要配置文件
    :return:
    """

    edit_id = request.GET.get("nid")
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    domains =models.CmdbInfo.objects.get(id=edit_id).domains
    name_war = models.CmdbInfo.objects.get(id=edit_id).name_war

    return HttpResponse('%stomcat部署完毕！'%(env.host_string))




def linux_put_task(request):
    """
    1、备份149上面的mcp，前提新建当天的文件夹目录$(date -d "today" +"%Y%m%d_%H%M%S")
    2、将从227上传的mcp拷贝至项目发布目录，解压war包并替换主要配置文件
    :return:
    """

    edit_id = request.GET.get("nid")
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    domains =models.CmdbInfo.objects.get(id=edit_id).domains
    name_war = models.CmdbInfo.objects.get(id=edit_id).name_war

    return HttpResponse('%slinux部署完毕！'%(env.host_string))

def port_reboot_task(request):
    form_obj=PortForm()
    mcp_port = models.WeblogicService.objects.filter(name='mcp').values('weblogicport__port'),
    mcp_port1 = [1,2,3],
    user = request.session.get('user_name')
    user_obj = request.session.get('user_avatar')
    print(user_obj)
    error_msg = ""
    if request.method == "GET":
        edit_id = request.GET.get("nid")
        hostlist = models.CmdbInfo.objects.get(id=edit_id)
        # return render(request, 'task_rebootportbak.html', {'user':user,'hostlist':hostlist,"user_obj":user_obj,'mcp_port':mcp_port,'mcp_port1':mcp_port1})
        return render(request, 'task_rebootportbak.html',{'form_obj':form_obj,'user':user,'user_obj':user_obj})

    else:
        form_obj = PortForm(request.POST)
        ret = {"status": 0, "msg": ""}
        if form_obj.is_valid():
            print(form_obj)
            # edit_id = request.POST.get("nid")
            edit_id = form_obj.cleaned_data.get('WeblogicPort')#根据name值获取对应的value值
            print(edit_id)
            env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip

            port = models.WeblogicPort.objects.get(nid=edit_id).port
            domains =models.CmdbInfo.objects.get(id=edit_id).domains
            print(env.host_string,port)

            ret["msg"] = "/api/mcp_operate_index/"
            return JsonResponse(ret)
            # sh_task = "cd %s/bin;sh %s_reboot.sh"%(domains,port)
            # print(form_obj)
            # result = run(sh_task, pty=False)
            # if result.return_code:
            #     return HttpResponse('no')
            # else:
            #     return HttpResponse('ok')


def linux_operate_task(request):
    form_obj=PortForm()
    mcp_port = models.WeblogicService.objects.filter(name='mcp').values('weblogicport__port'),
    mcp_port1 = [1,2,3],
    user = request.session.get('user_name')
    user_obj = request.session.get('user_avatar')
    print(user_obj)
    error_msg = ""
    if request.method == "GET":
        edit_id = request.GET.get("nid")
        hostlist = models.CmdbInfo.objects.get(id=edit_id)
        # return render(request, 'task_rebootportbak.html', {'user':user,'hostlist':hostlist,"user_obj":user_obj,'mcp_port':mcp_port,'mcp_port1':mcp_port1})
        return render(request, 'task_rebootportbak.html',{'form_obj':form_obj,'user':user,'user_obj':user_obj})

    else:
        form_obj = PortForm(request.POST)
        ret = {"status": 0, "msg": ""}
        if form_obj.is_valid():
            print(form_obj)
            # edit_id = request.POST.get("nid")
            edit_id = form_obj.cleaned_data.get('WeblogicPort')#根据name值获取对应的value值
            print(edit_id)
            env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip

            port = models.WeblogicPort.objects.get(nid=edit_id).port
            domains =models.CmdbInfo.objects.get(id=edit_id).domains
            print(env.host_string,port)

            ret["msg"] = "/api/linux_operate_index/"
            return JsonResponse(ret)
            # sh_task = "cd %s/bin;sh %s_reboot.sh"%(domains,port)
            # print(form_obj)
            # result = run(sh_task, pty=False)
            # if result.return_code:
            #     return HttpResponse('no')
            # else:
            #     return HttpResponse('ok')





#文件上传功能
from django.core.files.base import ContentFile
from django.core.files.storage import *
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def task_upload(request):
    user_id1 = request.session.get('user_id')
    user_obj = User.objects.filter(id=user_id1).values('avatar')
    user = request.session.get('user_name')
    if request.method == "POST":
        file_obj = request.FILES.get("upload")
        file_name = './upload/%s'%(file_obj.name)
        with open(file_name, "wb") as f:
            for line in file_obj.chunks():
                f.write(line)
    return render(request, "task_upload.html",{'user':user,'user_obj':user_obj[0]['avatar']})












