# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    created_date = models.DateTimeField(verbose_name = "Created On: ", auto_now_add = True)
    updated_date = models.DateTimeField(verbose_name = "Updated On: ", auto_now = True)
    published_date = models.DateTimeField(verbose_name = "Published On: ", default = timezone.now)

    def __unicode__(self):
        return "%s" % (self.title)    

class Ticker(models.Model):
    content = models.CharField(max_length = 200)
    visible = models.BooleanField(default = True)

    def __unicode__(self):
        return "%s" % (self.content)

class leftNavigation(models.Model):
    title = models.CharField(max_length = 100)
    link = models.URLField(max_length = 100)

class topNavigation(models.Model):
    title = models.CharField(max_length = 100)

class Execom(models.Model):
    chapter = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)