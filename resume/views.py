# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse, HttpResponseRedirect
from .models import Message
import os
from django.core.paginator import Paginator
from Utils.general import resume_ana


# Create your views here.
def index(request):
    context = resume_ana()
    return render(request, 'resume/resume.html', context)


def download_resuem(request):
    resume_path = os.path.join(os.path.join(settings.BASE_DIR, "media"), "resume.pdf")
    resume = open(resume_path, 'rb')
    response = FileResponse(resume)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="resume.pdf"'
    return response


def qq(request):
    return render(request, 'resume/qq.html')


def wechat(request):
    return render(request, 'resume/wechat.html')


def save_message(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    #保存留言到数据库
    lmessage = Message()
    lmessage.name = name
    lmessage.email = email
    lmessage.contents = message
    lmessage.save()

    return HttpResponseRedirect('/resume/show_message/')


def show_message(request):
    messages = Message.objects.all().order_by("-id")
    paginator = Paginator(messages, 5)
    pindex = request.GET.get("pindex", "")
    pindex = 1 if pindex == "" else int(pindex)
    page = paginator.page(pindex)
    return render(request, 'resume/message.html', {'messages': messages, 'page': page})
