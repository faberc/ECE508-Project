# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:20:27 2020

@author: Chuck
"""

import pyautogui

zoomUnmute = pyautogui.locateOnScreen('c:/Users/Chuck/Insync/kpfaber@gmail.com/Google Drive/Portland State University/Spring 2020/ECE 508 - Python Workshop/ECE508-Project/client/unmute2.png', confidence=0.9)
if (zoomUnmute != None):
    pyautogui.click(pyautogui.center(zoomUnmute))
else:
    print("Failed to find button.")