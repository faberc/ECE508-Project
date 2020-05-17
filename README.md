# ECE508-Project
Python project involving using a Raspberry Pi to light an indicator if my Zoom microphone is on to indicate to my husband not to bother me.

This script opens a socket to a Raspberry Pi. It also instantiates a GUI that looks for the Zoom meeting window. If the meeting window and the mute/unmute button is visible, it will be indicated on the GUI allowing the user to click the "Off Air" button which will search for the unmute button on the Zoom meeting window and click it.

## Dependencies:
pyautogui
openocd
time
threading
socket
tkinter
queue

## Setup and Running Script
1. In the client.py script, change the file path to the mute and unmute images as needed.
2. In the client.py script, change the host IP for the Raspberry Pi to what is appropriate for the Raspberry Pi on your network.
3. Access your Raspberry Pi and run the server.py script with `python server.py`.
4. On your PC run the client.py script with `python client.py`. The GUI should open up.
5. Open a Zoom meeting, and connect with audio. The GUI and the Zoom meeting should both be visible with no objects obstructing the Zoom mic button.
6. On the GUI click the “Off Air” button to go on air, and turn on the sign. To go off air, click the “On Air” button to toggle the mic off.

Note: The Zoom window must be on your primary screen if you have a multiple screen setup.