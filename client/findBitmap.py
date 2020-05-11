# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:02:14 2020

This test is not working.

@author: Chuck
"""


import autopy

def find_mic():
    mic = autopy.bitmap.Bitmap.open('unmute2.png')
    screen = autopy.bitmap.Bitmap.open('screencapture.png')
    
    pos = screen.find_bitmap(mic, 0.05)
    if pos:
        print("Found mic! %s" % str(pos))
    else:
        print("can't find")
    