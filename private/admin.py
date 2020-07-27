# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Journal
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Register your models here.
admin.site.register(Journal)
