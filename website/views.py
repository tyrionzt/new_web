#! coding: utf-8
from django.shortcuts import render
from resume.models import HomeIndex


def index(request):
    pretentious = "自知之明是最难得的知识。"
    faith = "生命中真正重要的不是你遭遇了什么,而是你记住了哪些事,又是如何铭记的  --《百年孤独》"
    insist = "生命的终结不是死亡，而是被遗忘  --《寻梦环游记》"
    skills = {"WEB DESIGN":
                "Python后端开发，熟悉Django和Flask框架，了解HTML，CSS, JS基本知识。能够利用Django独立开发网站并熟悉常见的网络安全问题",
              "SQL & NOSQL":
                "熟悉常见数据库的基本操作，熟悉MySQL的基本使用和调优，熟练使用非关系型数据库redis",
              "Liunx & 其它":
                "熟悉Linux常用命令，能在liunx下进行开发。熟悉多线程和多进程"}

    context = {"pretentious": pretentious, "faith": faith, "insist": insist, "skills": skills}
    return render(request, 'index/index.html', context)
