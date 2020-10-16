# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import json
aa = "/Users/tao/Documents/test.txt"
fp = open(aa, "rb")
ab = ""
for i in fp.readlines():
    ab = ab + i
print ab
