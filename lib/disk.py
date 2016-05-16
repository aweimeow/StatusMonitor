#! /usr/bin/python
# -*- coding: utf-8 -*-

import psutil


def disk_partitions():
    name = ['device', 'mountpoint', 'fstype', 'opts']
    r = list()
    for i in psutil.disk_partitions():
        r.append(dict(zip(name, i)))

    return r

def disk_usage():
    name = ['total', 'used', 'free', 'percent']

    return dict(zip(name, psutil.disk_usage('/')))

def disk_io_counter():
    name = ['read_count', 'write_count', 'read_bytes', 'write_bytes', 
            'read_time', 'write_time']

    return dict(zip(name, psutil.disk_io_counters()))

def disk_io_counters():
    name = ['read_count', 'write_count', 'read_bytes', 'write_bytes', 
            'read_time', 'write_time']
    r = dict()
    for key, value in psutil.disk_io_counters(perdisk=True).iteritems():
        r[key] = dict(zip(name, value))

    return r

