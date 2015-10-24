from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    author = models.ForeignKey('auth.User', related_name='posts')
    content = models.TextField(blank=True)
    categories = models.ManyToManyField("Category", related_name='posts')

    class Meta:
        ordering = ('created',)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('title',)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})
