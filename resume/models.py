# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.name


class ResumeContent(models.Model):
    motto = models.CharField(max_length=100)

    def __str__(self):
        return "简历内容"


class HomeIndex(models.Model):
    ip = models.CharField(max_length=16)  # 225.225.225.225
    ctime = models.DateTimeField(auto_now=True)
