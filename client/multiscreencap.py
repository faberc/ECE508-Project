# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:06:44 2020

@author: Chuck
"""


import wx
 
#app = wx.PySimpleApp()
app = wx.App()
 
context = wx.ScreenDC()
r, b = context.GetSize()
 
# Used for calculating the width of the resulting screenshot
#l, t = (-1360, 0) # coulfn't find a wx function to get these
l, t = (0, 0)
 
w, h = (r - l, b - t)
bitmap = wx.EmptyBitmap(w, h, -1)
 
memory = wx.MemoryDC()
memory.SelectObject(bitmap)

#memory.Blit(0, 0, w, h, context, l, t)
# Adjusted to match my resolution
memory.Blit(0, 0, w, h, context, -1920, t)

memory.SelectObject(wx.NullBitmap)
 
#bitmap.SaveFile("screencapture.bmp", wx.BITMAP_TYPE_BMP)
#bitmap.SaveFile("screencapture.jpg", wx.BITMAP_TYPE_JPEG)
bitmap.SaveFile("screencapture.png", wx.BITMAP_TYPE_PNG)
 