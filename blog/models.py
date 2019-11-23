from django.db import models
# Create your models here.
# class BlogUserInfo(User):
#     blog = models.OneToOneField(to="Blog", to_field="nid", null=True,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.username
class Blog(models.Model):
    """
    博客信息
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64,verbose_name = "个人博客标题")  # 个人博客标题
    site = models.CharField(max_length=32, unique=True,verbose_name = "个人博客后缀")  # 个人博客后缀
    theme = models.CharField(max_length=32,verbose_name = "博客主题")  # 博客主题

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "站点BLOG"
        verbose_name_plural = verbose_name

class Category(models.Model):
    """
    个人博客文章分类
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,verbose_name = "分类标题")  # 分类标题
    blog = models.ForeignKey(to="Blog", to_field="nid",on_delete=models.CASCADE)  # 外键关联博客，一个博客站点可以有多个分类

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章分类Category"
        verbose_name_plural = verbose_name

class Tag(models.Model):
    """
    标签
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32,verbose_name = "标签名")  # 标签名
    blog = models.ForeignKey(to="Blog", to_field="nid",on_delete=models.CASCADE,verbose_name = "所属博客")  # 所属博客

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "标签Tag"
        verbose_name_plural = verbose_name

class Article(models.Model):
    """
    文章
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,verbose_name = "文章标题")  # 文章标题
    desc = models.CharField(max_length=255,verbose_name = "文章描述")  # 文章描述
    create_time = models.DateTimeField()  # 创建时间

    category = models.ForeignKey(to="Category", to_field="nid", null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(to="api.User", to_field="id",on_delete=models.CASCADE)
    tags = models.ManyToManyField(  # 中介模型
        to="Tag",
        through="Article2Tag",
        through_fields=("article", "tag"),  # 注意顺序！！！
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章Article"
        verbose_name_plural = verbose_name

class ArticleDetail(models.Model):
    """
    文章详情表
    """
    nid = models.AutoField(primary_key=True)
    content = models.TextField()
    article = models.OneToOneField(to="Article", to_field="nid",on_delete=models.CASCADE)

    class Meta:
        verbose_name = "文章详情ArticleDetail"
        verbose_name_plural = verbose_name

class Article2Tag(models.Model):
    """
    文章和标签的多对多关系表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid",on_delete=models.CASCADE)
    tag = models.ForeignKey(to="Tag", to_field="nid",on_delete=models.CASCADE)

    class Meta:
        unique_together = (("article", "tag"),)
        verbose_name = "文章-标签Article2Tag"
        verbose_name_plural = verbose_name

class ArticleUpDown(models.Model):
    """
    点赞表
    """
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to="api.User", null=True,on_delete=models.CASCADE)
    article = models.ForeignKey(to="Article", null=True,on_delete=models.CASCADE)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = (("article", "user"),)
        verbose_name = "文章点赞ArticleUpDown"
        verbose_name_plural = verbose_name

class Comment(models.Model):
    """
    评论表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid",on_delete=models.CASCADE)
    user = models.ForeignKey(to="api.User", to_field="id",on_delete=models.CASCADE)
    content = models.CharField(max_length=255)  # 评论内容
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", null=True,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "评论Comment"
        verbose_name_plural = verbose_name