# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse,HttpResponseRedirect
from .models import Message

# Create your views here.
def index(request):
    return render(request, 'resume/resume.html')

def download_resuem(request):
    file = open(settings.BASE_DIR + '/resume.pdf', 'rb')
    # return HttpResponse("it's ok")
    response = FileResponse(file)
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

    return HttpResponseRedirect('/')

def show_message(request):
    messages = Message.objects.all()
    return render(request, 'resume/message.html', {'messages': messages})