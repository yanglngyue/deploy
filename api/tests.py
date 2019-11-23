from django.test import TestCase

# Create your tests here.
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deploy.settings")# project_name 项目名称
django.setup()

from api import models


def img():
    user_obj = models.User.objects.values('avatar').filter(id=4)
    print(user_obj)
img()
# # 查找所有书名里包含番茄的书
#
# v1 = models.Book.objects.filter(title__contains ="番茄")
# print(v1)
#
# # 查找出版日期是2017年的书
# v2 = models.Book.objects.filter(publish_date__year='2017')
# print(v2)
#
#
# # 查找出版日期是2017年的书名
# v3 = models.Book.objects.filter(publish_date__year='2017')
# print(v3)
#
#
#
# # 查找价格大于10元的书
# v4 = models.Book.objects.filter(price__gt=10)
#
# print(v4)
# # 查找价格大于10元的书名和价格
# v5 = models.Book.objects.filter(price__gt=10).values('title','price')
# print(v5)
#
# # 查找memo字段是空的书
#
# v6 = models.Book.objects.filter(memo__isnull='null').all()
# print(v6)
#
# #
# # 查找在北京的出版社
# v7 = models.Publisher.objects.filter(city__contains='北京')
# print(v7)
#
#
# # 查找名字以沙河开头的出版社
# v8 = models.Publisher.objects.filter(name__istartswith='沙河')
# print(v8)
#
# #
# # 查找作者名字里面带“小”字的作者
# v9 = models.Author.objects.filter(name__icontains='小')
#
# print(v9)
#
# # 查找年龄大于30岁的作者
# v10 = models.Author.objects.filter(age__gt=30)
# print(v10)
#
# # 查找手机号是155开头的作者
# v11 = models.Author.objects.filter(phone__istartswith='155')
# print(v11)
#
# # 查找手机号是155开头的作者的姓名和年龄
# v12 = models.Author.objects.filter(phone__istartswith='155').values('name','age')
# print(v12)
# # 查找书名是“番茄物语”的书的出版社
# v13 = models.Book.objects.filter(title='番茄物语').values("publisher__name")
# print(v13)
#
#
# # 查找书名是“番茄物语”的书的出版社所在的城市
# # v14 = models.Book.objects.get(title='番茄物语')
# # # print(v14.publisher_id)
# # # print(models.Publisher.objects.filter(id=v14.publisher_id).values('name','city'))
# v14 = models.Book.objects.filter(title='番茄物语').values("publisher__city")
# print(v14)
#
# # 查找书名是“番茄物语”的书的出版社的名称
# #
# v15 = models.Book.objects.filter(title='番茄物语').values("publisher__name")
#
#
# # 查找书名是“番茄物语”的书的所有作者
# v16 = models.Book.objects.filter(title='番茄物语').values("author__name")
# print(v16)
#
#
#
# # 查找书名是“番茄物语”的书的作者的年龄
#
# v17 = models.Book.objects.filter(title='番茄物语').values("author__age")
# print(v17)
#
# # 查找书名是“番茄物语”的书的作者的手机号码
# v18 = models.Book.objects.filter(title='番茄物语').values("author__phone")
# print(v18)
# #
# # 查找书名是“番茄物语”的书的作者的地址
# v19 = models.Book.objects.filter(title='番茄物语').values("author__detail__addr")
# print(v19)
#
# # 查找书名是“番茄物语”的书的作者的邮箱
#
#
# v20 = models.Book.objects.filter(title='番茄物语').values("author__detail__email")
# print(v20)
from cmdb import models
from api import models
from fabric.api import *
import time
# env.hosts = ['10.10.68.149',]

# env.password = 'super123'
env.key_filename = '/home/linux/.ssh/id_rsa'
env.user = 'super'
# def remote_task():
#     with cd('/home'):     # with 的左右是让后面的表达式，继承前面的状态
#         run('mkdir /home/weblogic/yanglongyue201911041518.txt')
#         return run
# print(remote_task())
# def upload_file():
#     return 'ok'
# print(upload_file())
#
#
# def check():
#     a = models.Partment.objects.get(id=2)
#     print(a)
# check()
#
#
#






from cmdb.models import *

a= WeblogicPort.objects.all().values_list("nid", "port")
print(a)
# mcp_port1 = WeblogicService.objects.filter(name='mcp').values("weblogicport__port"),
# print(mcp_port1)
# for i in mcp_port1:
#     print(i))