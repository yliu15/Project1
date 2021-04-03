#!/usr/bin/python
# --*-- coding:utf-8 --*--


import re
import sys

pat = re.compile('[0-1][0-9][0-5][0-9][AP]')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        print'%s\t%s' %(match.group(),1)
