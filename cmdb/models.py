from django.db import models

# Create your models here.
class CmdbInfo(models.Model):
    PLATFORM_CHOICES = (
        ("移动查勘", "移动查勘"),
        ("移动协赔", "移动协赔"),
        ("华为云", "华为云"),
        ("小微", "小微"),
        ("流程控制平台", "流程控制平台"),
        ("其他", "其他")
    )
    REGION_CHOICES = (
        ("香港", '香港'),
        ("东京", '东京'),
        ("华北2", '华北2'),
        ("佛山", '南中心'),
        ("其他", '其他')
    )
    WEBLOGIC_AUTHOR = (
            ("主管", '主管'),
            ("受管", '受管'),

    )

    hostname = models.CharField(max_length=64, verbose_name='主机名', unique=True)
    F5 = models.GenericIPAddressField(verbose_name='F5', unique=True, null=True, blank=True)
    network_ip = models.GenericIPAddressField(verbose_name='内网IP', unique=True, null=True, blank=True)
    inner_ip = models.GenericIPAddressField(verbose_name='外网IP', null=True, blank=True)
    system = models.CharField(max_length=128, verbose_name='系统版本', null=True, blank=True)
    cpu = models.CharField(max_length=64, verbose_name='CPU', null=True, blank=True)
    memory = models.CharField(max_length=64, verbose_name='内存', null=True, blank=True)
    disk = models.CharField(max_length=256, verbose_name="硬盘", null=True, blank=True)
    platform = models.CharField(max_length=128, choices=PLATFORM_CHOICES, verbose_name='项目组')
    region = models.CharField(max_length=128, choices=REGION_CHOICES, verbose_name='机房位置')
    # weblogic = models.CharField(max_length=128, choices=WEBLOGIC_AUTHOR, verbose_name='服务类别')
    # weblogic_port = models.IntegerField(verbose_name="服务端口",  null=True, blank=True)
    ps = models.CharField(max_length=1024, verbose_name="备注", null=True, blank=True)
    port = models.IntegerField(verbose_name="登录端口", default='22', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='服务状态')
    name_war = models.CharField(max_length=128, verbose_name='项目包路径',null=True, blank=True)
    domains = models.CharField(max_length=1024, verbose_name="域路径", null=True, blank=True)

    ctime = models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间', blank=True)
    utime = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间', blank=True)


class WeblogicService(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='应用名', unique=True)
    weblogicport = models.ManyToManyField(to="WeblogicPort")
    def __str__(self):
        return self.name
class WeblogicPort(models.Model):
    nid = models.AutoField(primary_key=True)
    port = models.IntegerField(verbose_name="应用端口", null=True, blank=True)
    def __str__(self):
        return self.port