# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Journal(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=20, default="tyrion")

    def __str__(self):
        return "%s" % self.title


class ZhushiTest(models.Model):
    name = models.CharField(max_length=10, help_text="哈哈")
    password = models.CharField(max_length=100, help_text="嘿嘿")
