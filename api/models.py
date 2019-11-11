from django.db import models

# Create your models here.



# 书
class Book(models.Model):
    title = models.CharField(max_length=32)
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    memo = models.TextField(null=True)
    # 创建外键，关联publish
    publisher = models.ForeignKey(to="Publisher",on_delete=models.CASCADE)
    # 创建多对多关联author
    author = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


# 出版社
class Publisher(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    def __str__(self):
        return self.name


# 作者
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    detail = models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 作者详情
class AuthorDetail(models.Model):
    addr = models.CharField(max_length=64)
    email = models.EmailField()

#用户表
class User(models.Model):
    username=models.CharField(max_length=16)
    password=models.CharField(max_length=32)

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



