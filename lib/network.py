#! /usr/bin/python
# -*- coding: utf-8 -*-

import psutil


def network_io_counters():
    name = ['byte_sent', 'byte_recv', 'packet_sent', 'packet_recv', 'errin', 
            'errout', 'dropin', 'dropout']
    r = dict()
    for key, value in psutil.net_io_counters(pernic=True).iteritems():
        r[key] = dict(zip(name, value))

    return r

def net_if_addrs():
    name = ['family', 'address', 'netmask', 'broadcast', 'ptp']
    r = dict()
    for key, value in psutil.net_if_addrs().iteritems():
        r[key] = dict(zip(name, value))

    return r

def net_if_stats():
    name = ['isup', 'duplex', 'speed', 'mtu']
    r = dict()
    for key, value in psutil.net_if_stats().iteritems():
        r[key] = dict(zip(name, value))

    return r
