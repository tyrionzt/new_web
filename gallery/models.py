# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from website.fields import ThumbnailImageField

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=249)
    desc = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ('item_detail', None, {'pk': self.id})


class Photo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=249, blank=True)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return ('photo_detail', None, {'pk': self.id})
