#! coding: utf-8
from django.shortcuts import render
from Utils.general import record_ip, home_ana
from resume.models import HomeIndex


def index(request):
    record_ip(HomeIndex, request)
    context = home_ana()
    return render(request, 'index/index.html', context)
