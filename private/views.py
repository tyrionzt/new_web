# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from .models import Journal
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    pindex = request.GET.get("page", "")
    essay_type = request.GET.get("type", "技术笔记")
    print(essay_type)
    pindex = 1 if pindex == "" else int(pindex)

    contents = Journal.objects.filter(type=essay_type).order_by("-id")
    pages = len(contents) // 5 if len(contents) % 5 == 0 else len(contents) // 5 + 1
    show_contents = contents[(pindex * 5 - 5):(pindex * 5)]
    context = {"contents": show_contents, "page": pindex, "essay": essay_type, "pages": pages}
    return render(request, "private/index.html", context)


def query_journal(request):
    key = request.POST.get("key")
    pindex = request.POST.get("page", "")
    print request.POST
    essay_type = request.POST.get("type", "技术笔记")
    print "查询的内容为： ", essay_type
    pindex = 1 if pindex == "" else int(pindex)
    contents = Journal.objects.filter(type=essay_type).filter(Q(author__icontains=key) | Q(contents__icontains=key))
    pages = len(contents) // 5 if len(contents) % 5 == 0 else len(contents) // 5 + 1
    show_contents = contents[(pindex*5 - 5):(pindex*5)]
    context = {"contents": show_contents, "page": pindex, "essay": essay_type, "pages": pages, "query": True}
    return render(request, "private/index.html", context)


def detail_journal(request):
    jou_id = request.GET.get("id")
    contents = Journal.objects.get(id=jou_id)
    context = {"contents": contents}
    return render(request, 'private/detail.html', context)


def like_journal(request):
    pass