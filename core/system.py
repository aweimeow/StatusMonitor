#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
from subprocess import Popen, PIPE


def getIP(interface):
    p = Popen('ifconfig %s' % interface, stdout=PIPE, stderr=PIPE, shell=True)
    stdout = p.communicate()[0]
    r = re.search('inet addr:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', stdout)
    ip = r.group(1)
    return ip
