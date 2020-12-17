# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os


# Create your views here.
def index(request):
    return render(request, 'fun/index.html')


def show_recode(request):
    name = request.GET.get('name')
    html = 'fun/' + name + '.html'
    return render(request, html)


def download_game(request):
    name = request.GET.get('name')
    game_path = os.path.join(os.path.join(os.path.join(settings.BASE_DIR + "media"), "games"), name + ".zip")
    fp = open(game_path, 'rb')
    response = FileResponse(fp)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s.zip"' % name
    return response

