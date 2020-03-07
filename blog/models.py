from django.contrib.auth.models import User
from django.db import models


# 导入Django自带用户模块


# Create your models here.
# 基类
class BaseModel(models.Model):
    create_date = models.DateField(auto_now_add=True, verbose_name='创建日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')

    class Meta:
        abstract = True


# 创建文章分类模型
class Category(BaseModel):
    name = models.CharField(max_length=128, verbose_name='博客文章分类')
    index = models.IntegerField(default=0, verbose_name='分类排序')

    class Meta:
        db_table = 'tbl_category'
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签
class Tag(BaseModel):
    name = models.CharField(max_length=128, verbose_name='文章标签')

    class Meta:
        db_table = 'tbl_tag'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Tui 推荐位
class Tui(BaseModel):
    name = models.CharField(max_length=128, verbose_name='推荐位')

    class Meta:
        db_table = 'tbl_tui'
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(BaseModel):
    title = models.CharField(max_length=128, verbose_name='文章标题')
    excerpt = models.TextField(max_length=200, blank=True, verbose_name='摘要')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='博客分类')
    # 使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    img = models.ImageField(upload_to='%Y/%m/%d/', blank=True, null=True, verbose_name='图片')
    body = models.TextField(verbose_name='文章主体')
    """
         文章作者，这里User是从django.contrib.auth.models导入的。
         这里我们通过 ForeignKey 把文章和 User 关联了起来。
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='推荐位')

    class Meta:
        db_table = 'tbl_article'
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title


# 轮播图Banner
class Banner(BaseModel):
    text_info = models.CharField(max_length=128, default='', verbose_name='标题')
    img = models.ImageField(upload_to='banner/', verbose_name='轮播图')
    link_url = models.URLField(max_length=128, verbose_name='图片链接')
    is_active = models.BooleanField(default=False, verbose_name='是否是Article')

    class Meta:
        db_table = 'tbl_banner'
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

    def __str__(self):
        return self.text_info


# 友情链接
class Link(BaseModel):
    name = models.CharField(max_length=20, verbose_name='链接名称')
    linkurl = models.URLField(max_length=128, verbose_name='网址')

    class Meta:
        db_table = 'tbl_link'
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'

    def __str__(self):
        return self.name
