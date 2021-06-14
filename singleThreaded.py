# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 20:43:01 2021

@author: ASHUTOSH
"""

# single_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)