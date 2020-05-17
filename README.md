# ECE508-Project
Python project involving using a Raspberry Pi to light an indicator if my Zoom microphone is on to indicate to my husband not to bother me.

This script opens a socket to a Raspberry Pi. It also instantiates a GUI that looks for the Zoom meeting window. If the meeting window and the mute/unmute button is visible, it will be indicated on the GUI allowing the user to click the "Off Air" button which will search for the unmute button on the Zoom meeting window and click it.

## Libraries Used:
pyautogui
openocd
time
threading
socket
tkinter
queue

