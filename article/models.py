from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

class Article(models.Model) :
    title = models.CharField(max_length = 50)  #博客题目
    tags = models.ManyToManyField(Tag)  #博客分类 可为空
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    taglist = []

    #获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self) :
        return self.title

    def save(self, *args, **kwargs):
        super(Article, self).save()
        for i in self.taglist:
            p, created = Tag.objects.get_or_create(tag_name=i)
            self.tags.add(p)

    class Meta:
        ordering = ['-date_time']

