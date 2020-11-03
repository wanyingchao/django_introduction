from django.db import models


# Create your models here.


class Article(models.Model):
    # 文章的唯一ID，设置为主键增长
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章主要内容
    content = models.TextField()
    # 文章的发布日期，默认当前时间
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # 返回文章标题
        return self.title
