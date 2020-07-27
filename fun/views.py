# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, 'fun/index.html')


def show_rcode(request):
    name = request.GET.get('name')
    html = 'fun/' + name + '.html'
    print html
    return render(request, html)


def download_game(request):
    name = request.GET.get('name')
    game = settings.BASE_DIR + '/media/games/' + name + ".zip"
    file = open(game, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s.zip"'%name
    return response

