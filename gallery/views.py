# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Item, Photo
# Create your views here.


class IndexView(object):

    def get_queryset(self, request):
        contents = Item.objects.all().order_by("-id")
        context = {"contents": contents}
        return render(request, "gallery/index.html", context)

    def photo_detail(self, request):
        item_id = request.GET.get("id")
        item = Item.objects.get(id=item_id)
        photos = item.photo_set.all()
        context = {"contents": photos, "item": item}
        return render(request, "gallery/detail.html", context)
