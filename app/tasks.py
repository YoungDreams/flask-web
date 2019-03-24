# _*_ coding: utf-8 _*_
__author__ = 'taylor'
__date__ = '2019/3/25 12:13 AM'

import time

def example(seconds):
    print('Starting task')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Task completed')