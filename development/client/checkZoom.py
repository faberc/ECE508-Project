import psutil, threading

def verifyZoom():
    zoomOn = False
    for pid in psutil.pids():
        p = psutil.Process(pid)
        print(p.name())
        if p.name() == "Zoom.exe":
            zoomOn = True
    print(zoomOn)


t1 = threading.Thread(target=verifyZoom)

t1.start()