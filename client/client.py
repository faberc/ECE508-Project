import pyautogui, time, threading, socket, psutil, tkinter as tk
from queue import Queue

class onAirGUI:
    """ GUI and methods for Zoom On Air Sign"""

    def __init__(self):
        """Declare State Variables"""
        self.zoomOn = False
        self.rPiConnected = False
        self.micOn = False
        self.ledOn = False
        self.onAir = False
        self.zoomMicButton = None
        
        """Create tkinter object"""
        self.root = tk.Tk()
        self.root.title("Zoom Mic Control")

        """Declare string variables"""
        self.zoomStatus = tk.StringVar()
        self.rPiStatus = tk.StringVar()
        self.micStatus = tk.StringVar()
        self.ledStatus = tk.StringVar()
        self.buttonText = tk.StringVar()

        """Initialize Widgets"""
        self.zoomLabel = tk.Label(self.root, textvariable=self.zoomStatus)
        self.zoomLabel.grid(row=0, column=0, sticky='w')

        self.rPiLabel = tk.Label(self.root, textvariable=self.rPiStatus)
        self.rPiLabel.grid(row=0, column=9, sticky='e')

        self.airButton = tk.Button(self.root, textvariable=self.buttonText, command=self.buttonPress)
        self.airButton.grid(row=1, column=0, columnspan=10, sticky='e'+'w', padx=5, pady=5)

        self.micIndic = tk.Radiobutton(self.root, state='disabled', textvariable=self.micStatus)
        self.micIndic.grid(row=2, column=0, sticky='w')

        self.ledLabel = tk.Label(self.root, textvariable=self.ledStatus)
        self.ledLabel.grid(row=2, column=9, sticky='e')

        self.root.grid_columnconfigure(4, minsize=100)

        """Host and Port Definitions"""
        self.__HOST = '10.0.1.87'
        self.__PORT = 12345

        """Initialize Queue"""
        self.q = Queue(maxsize=0)

        """Initialize Socket"""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.__HOST,self.__PORT))
        self.rPiConnected = True

        self.sockThread = threading.Thread(target=self.socketListen)
        self.zoomThread = threading.Thread(target=self.checkZoom)

        self.sockThread.start()
        self.zoomThread.start()

        self.updateLabels()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.mainloop()

    def killall(self):
        self.q.put("quit")
        self.close()

    def close(self):
        self.sockThread.join()
        self.zoomThread.join()
        self.root.destroy()

    def checkZoom(self):
        while True:
            for pid in psutil.pids():
                try:
                    p = psutil.Process(pid)
                except:
                    print("failed to get pid")
                if p.name() == "Zoom.exe":
                    self.zoomOn = True
                else:
                    self.zoomOn = False
            time.sleep(10)

    def socketListen(self):
        while True:
            if not self.q.empty():
                command = self.q.get()
                command = command.encode('utf-8')
                self.s.sendall(command)
                reply = self.s.recv(1024)
                reply = reply.decode('utf-8')
                print(reply)
                if reply == 'led on':
                    self.ledOn = True
                elif reply == 'led off':
                    self.ledOff = False
                elif reply == 'Terminating':
                    break

    def updateLabels(self):
        if self.zoomOn is True:
            self.zoomStatus.set("Zoom On")
            self.zoomLabel.config(fg='green')
        else:
            self.zoomStatus.set("Zoom Off")
            self.zoomLabel.config(fg='red')


        if self.rPiConnected is True:
            self.rPiStatus.set("Pi Connected")
            self.rPiLabel.config(fg='green')
        else:
            self.rPiStatus.set("Pi Disconnected")
            self.rPiLabel.config(fg='red')

        if self.micOn is True:
            self.micStatus.set("Mic On")
            self.micIndic.config(disabledforeground='red')
            self.micIndic.select()
        else:
            self.micStatus.set("Mic Off")
            self.micIndic.config(disabledforeground='gray')
            self.micIndic.deselect()

        if self.onAir is True:
            self.buttonText.set("On Air")
            self.airButton.config(relief='sunken', foreground='red')
        else:
            self.buttonText.set("Off Air")
            self.airButton.config(relief='raised', foreground='black')

        if self.ledOn is True:
            self.ledStatus.set("LED On")
            #ledLabel.config(fg='red')
        else:
            self.ledStatus.set("LED Off")
            #ledLabel.config(fg='black')

        self.root.after(1, self.updateLabels)
    
    def buttonPress(self):
        if not self.onAir:
            self.zoomMicButton = pyautogui.locateOnScreen('c:/Users/Chuck/Insync/kpfaber@gmail.com/Google Drive/Portland State University/Spring 2020/ECE 508 - Python Workshop/ECE508-Project/client/unmute3.png', confidence=0.9)
            if self.zoomMicButton is not None:
                pyautogui.click(pyautogui.center(self.zoomMicButton))
                self.q.put("on")
                self.onAir = True
                self.micOn = True
            else:
                print("Failed to find button.")

        else:
            self.zoomMicButton = pyautogui.locateOnScreen('c:/Users/Chuck/Insync/kpfaber@gmail.com/Google Drive/Portland State University/Spring 2020/ECE 508 - Python Workshop/ECE508-Project/client/mute2.png', confidence=0.9)
            if self.zoomMicButton is not None:
                pyautogui.click(pyautogui.center(self.zoomMicButton))
                self.q.put("off")
                self.onAir = False
                self.micOn = False
            else:
                print("Failed to find button.")


gui = onAirGUI()