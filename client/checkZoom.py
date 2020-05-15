import psutil

def verifyZoom():
    zoomOn = False
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == "Zoom.exe":
            zoomOn = True
            break
    print(zoomOn)

verifyZoom()