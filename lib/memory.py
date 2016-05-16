#! /usr/bin/python
# -*- coding: utf-8 -*-

import psutil


def virtual_memory():
    name = ['total', 'available', 'percent', 'used', 'free', 'active', 
            'inactive', 'buffers', 'cached', 'shared']
    return dict(zip(name, psutil.virtual_memory()))

def swap_memory():
    name = ['total', 'used', 'free', 'percent', 'sin', 'sout']
    return dict(zip(name, psutil.swap_memory()))
