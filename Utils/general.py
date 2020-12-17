#! coding: utf-8
"""
主要用于写一些通用方法。获取时间，字符串处理，参数校验等等
"""


def record_ip(HomeIndex, request):
    """
    记录访问者的ip
    :param HomeIndex:
    :param request:
    :return:
    """
    ip_save = HomeIndex()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP
    ip_save.ip = ip
    ip_save.save()


def home_ana():
    """
    展示在首页的名言集，用一个特定方法来写，方便修改
    :return:
    """
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
    return context


def resume_ana():
    """
    更新简历中的个人信息
    :return:
    """
    motto = "满招损，谦受益！"
    return {"motto": motto}
