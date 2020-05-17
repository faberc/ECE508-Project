import tkinter as tk
from time import sleep

zoomOn = True
rPiConnected = True
micOn = False
ledOn = False
onAir = False

def buttonPress():
    global onAir, micOn, ledOn
    onAir = not onAir
    micOn = not micOn
    ledOn = not ledOn

    if onAir is True:
        buttonText.set("On Air")
        airButton.config(relief='sunken', foreground='red')
    else:
        buttonText.set("Off Air")
        airButton.config(relief='raised', foreground='black')

def updateLabels():
    if zoomOn is True:
        zoomStatus.set("Zoom On")
        zoomLabel.config(fg='green')
    else:
        zoomStatus.set("Zoom Off")
        zoomLabel.config(fg='red')

    
    if rPiConnected is True:
        rPiStatus.set("Pi Connected")
        rPiLabel.config(fg='green')
    else:
        rPiStatus.set("Pi Disconnected")
        rPiLabel.config(fg='red')

    if micOn is True:
        micStatus.set("Mic On")
        micIndic.config(disabledforeground='red')
        micIndic.select()
    else:
        micStatus.set("Mic Off")
        micIndic.config(disabledforeground='gray')
        micIndic.deselect()

    if ledOn is True:
        ledStatus.set("LED On")
        #ledLabel.config(fg='red')
    else:
        ledStatus.set("LED Off")
        #ledLabel.config(fg='black')

    root.after(1, updateLabels)

root = tk.Tk()
root.title("Zoom Mic Control")


zoomStatus = tk.StringVar()
rPiStatus = tk.StringVar()
micStatus = tk.StringVar()
ledStatus = tk.StringVar()
buttonText = tk.StringVar()

zoomStatus.set("Zoom Status")
zoomLabel = tk.Label(root, textvariable=zoomStatus)
zoomLabel.grid(row=0, column=0, sticky='w')

rPiStatus.set("RPi Status")
rPiLabel = tk.Label(root, textvariable=rPiStatus)
rPiLabel.grid(row=0, column=9, sticky='e')

buttonText.set("Off Air")
airButton = tk.Button(root, textvariable=buttonText, command=buttonPress)
airButton.grid(row=1, column=0, columnspan=10, sticky='e'+'w', padx=5, pady=5)

micStatus.set("Mic On")
micIndic = tk.Radiobutton(root, state='disabled', textvariable=micStatus)
micIndic.grid(row=2, column=0, sticky='w')

ledStatus.set("LED Status")
ledLabel = tk.Label(root, textvariable=ledStatus)
ledLabel.grid(row=2, column=9, sticky='e')


root.grid_columnconfigure(4, minsize=100)

updateLabels()
root.mainloop()
