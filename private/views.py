# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from .models import Journal
from django.db.models import Q

# Create your views here.


def index(request):
    contents = Journal.objects.all().order_by("-id")
    context = {"contents": contents}
    return render(request, 'private/index.html', context)


def create_journal(request):
    title, describe, author = request.POST.get("title"), request.POST.get("describe"), request.POST.get("author")
    journal = Journal()
    journal.title, journal.describe, journal.author = title, describe, author
    journal.save()
    return HttpResponseRedirect('/private')


def update_journal(request):
    return create_journal(request)


def delete_journal(request):
    Journal.objects.filter(id=request.POST.get("id")).delete()
    return HttpResponseRedirect('/private')


def query_journal(request):
    key = request.POST.get("key")
    contents = Journal.objects.filter(Q(author__icontains=key) | Q(title__icontains=key) |
                                      Q(describe=key))
    context = {"contents": contents}
    return render(request, "private/index.html", context)


def detail_journal(request):
    jou_id = request.GET.get("id")
    contents = Journal.objects.get(id=jou_id)
    context = {"contents": contents}
    return render(request, 'private/detail.html', context)
