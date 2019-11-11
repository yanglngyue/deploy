#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/11/1 0001 16:34
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deploy.settings")# project_name 项目名称
django.setup()

from utils.check_login import check_login,require_login
from django.shortcuts import render,redirect,HttpResponse,render_to_response
from api import models
from cmdb import models
from utils.pager import PageInfo
from fabric.api import *
import time
ctime = "`date +%Y%m%d_%H%M%S`"
date_time= "`date +%Y%m%d`"
env.user = 'super'
# env.hosts = ['10.10.68.149']
# env.password = 'super123'
# env.host_string = '10.10.68.149'
# env.host_string = models.CmdbInfo.objects.values('network_ip')
env.key_filename = '/home/linux/.ssh/id_rsa'

def task_index(request):
    all_count = models.CmdbInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 10, 'task_push.html', 11)
    ip_list = models.CmdbInfo.objects.all()[page_info.start():page_info.end()]
    return render(request,'task_push.html',{'ip_list':ip_list,'page_info':page_info})


def task_work(request):
    """
    请先在所有服务器创建/deploy文件夹,项目包路径/backup,/initconfig,停止脚本及启动脚本
    1、拷贝119上面的mcp.war到227本地
    2、227上面的mcp.war拷贝到149上面的/deploy下
    :return:
    """
    edit_id = request.GET.get("nid")
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    print(env.host_string)
    scp = "scp super@10.10.1.119:/home/samba/移动理赔平台V5050提测资料/interfaceUseServer.csv ./"
    scp_put = "scp ./* %s@%s:/deploy/%s"%(env.user,env.host_string,date_time)
    run('rm -rf /deploy/*;mkdir -p /deploy/`date +%Y%m%d`')
    mkcd = 'function __mkcd(){ if [ $# == 1 ]; then mkdir $1; cd $1; unset -f __mkcd; elif [ $# == 2 ]; then mkdir $1 $2; cd $2; unset -f __mkcd; fi }; __mkcd'
    local('%s /home/linux/apphome/%s;%s;%s'%(mkcd,ctime,scp,scp_put))
         #"with"的作用是让后面的表达式的语句继承当前状态，实现"cd /root/ && ls -l'的效果
    return HttpResponse('149冻结环境mcp环境初始化完毕！')



def put_task(request):
    """
    1、备份149上面的mcp，前提新建当天的文件夹目录$(date -d "today" +"%Y%m%d_%H%M%S")
    2、将从227上传的mcp拷贝至项目发布目录，解压war包并替换主要配置文件
    :return:
    """

    edit_id = request.GET.get("nid")
    env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
    domains =models.CmdbInfo.objects.get(id=edit_id).domains
    name_war = models.CmdbInfo.objects.get(id=edit_id).name_war
    run('cp -rf %s/mcp %s/backup/%s'%(name_war,name_war,ctime))
    run('rm -rf %s/mcp/*'%(name_war))
    run('cp -rf /deploy/%s/mcp.war %s/mcp/'%(date_time,name_war))
    time.sleep(5)
    with cd('%s/mcp'%(name_war)):
        run('jar -xvf mcp.war')
        run('cp -rf %s/initconfig/* %s/mcp/WEB-INF/classes/'%(name_war,name_war))

    return HttpResponse('149冻结环境mcp部署完毕！')
# def change_paper(chage_papername,chage_path):
#     cp = "cp -rf %s %s"%(chage_papername,chage_path)
#     with cd('/home/middleware/apphome/mcp/WEB-INF/classes/'):
#         run(cp)
def reboot_task(request):
    error_msg = ""
    if request.method == "GET":
        edit_id = request.GET.get("nid")
        hostlist = models.CmdbInfo.objects.get(id=edit_id)
        return render(request, 'task_rebootport.html', {"error": error_msg,'hostlist':hostlist})
    else:

        # port = 8002
        # kill_pid = "ps -ef|grep java|grep ManagedServer%s|awk '{print $2}'||xargs kill -9"%(port)
        # sh_task = "sh /home/weblogic/domains/mcp_domain/bin/startManaged%s.sh"%(port)
        # tailf_log = "tailf /home/weblogic/domains/mcp_domain/log/%s/ManagedServer%s.out"%(port,port)
        # run(kill_pid)
        # print("程序已杀死，3秒后重启。。。。")
        # time.sleep(3)
        # run(sh_task)
        # print("启动脚本执行，以下为实时输出日志")
        # time.sleep(2)
        # run(tailf_log)
        # return HttpResponse('149冻结环境mcp服务重启完毕！')
        edit_id = request.POST.get("nid")
        env.host_string = models.CmdbInfo.objects.get(id=edit_id).network_ip
        port = request.POST.get("port", None)
        domains =models.CmdbInfo.objects.get(id=edit_id).domains
        print(env.host_string,port)
        # kill_pid = "ps -ef|grep java|grep ManagedServer%s|awk '{print $2}'|xargs kill -9"%(port)
        sh_task = "sh %s/bin/%s_stop.sh"%(domains,port)
        start_sh = "cd %s/bin;sh startManaged%s.sh"%(domains,port)
        run(sh_task)
        run(start_sh)
        if run:
            time.sleep(3)
            return HttpResponse('ok')
        else:
            return HttpResponse('%smcp服务重启失败！' % (port))


