from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class BlogCategory(models.Model):
    title = models.CharField('Title', max_length=250)
    slug = models.SlugField('Slug Url',unique=True)
    published = models.BooleanField(default=True)
    date = models.DateTimeField('Published Date', default = timezone.now())
    def __str__(self):
        return self.title
    def getPostCount(self):
        return self.blogpost_set.count()


class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=True)
    teaser = models.TextField(blank=True)
    content = HTMLField()
    date = models.DateTimeField('Publised Date', default = timezone.now())
    categories = models.ManyToManyField(BlogCategory,blank=True, null=False)
    def __str__(self):
	    return self.title
