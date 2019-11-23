from django.db import models
# Create your models here.

#用户表
class User(models.Model):
    username=models.CharField(max_length=16)
    password=models.CharField(max_length=32,default="123")
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=11,null=True)
    avatar = models.FileField(upload_to="avatars/", default="avatars/default.png", verbose_name="头像")
    blog = models.OneToOneField(to="blog.Blog", to_field="nid", null=True,on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "用户信息表User"
        verbose_name_plural = verbose_name
#升级版本记录表
class Promotion(models.Model):
    name = models.CharField(max_length=1024, verbose_name="版本名称", null=True, blank=True)
    select = models.CharField(max_length=1024, verbose_name="升级类型", null=True, blank=True)
    extent = models.CharField(max_length=1024, verbose_name="升级范围", null=True, blank=True)
    info = models.CharField(max_length=1024, verbose_name="升级内容", null=True, blank=True)
    uptime = models.DateTimeField(auto_now_add=True, null=True, verbose_name='升级时间', blank=True)
    ps = models.CharField(max_length=1024, verbose_name="备注", null=True, blank=True)


    def __str__(self):
        return self.name

# 部门表
class Partment(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

