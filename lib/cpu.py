#! /usr/bin/python
# -*- coding: utf-8 -*-

import psutil


def cpu_count():
    return psutil.cpu_count()

def cpu_use_percent():
    return psutil.cpu_percent()

def cpu_use_percents():
    return psutil.cpu_percent(percpu=True)

def cpu_time():
    name = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 
            'steal', 'guest', 'guest_nice']
    return dict(zip(name, psutil.cpu_times()))

def cpu_times():
    name = ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 
            'steal', 'guest', 'guest_nice']
    r = list()
    for i in psutil.cpu_times(percpu=True):
        r.append(dict(zip(name, i)))
    return r

def cpu_stat():
    name = ['ctx_switches', 'interrupts', 'soft_interrupts', 'syscalls']
    return dict(zip(name, psutil.cpu_stats()))
