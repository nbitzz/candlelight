from cefpython3 import cefpython as cef
import tkinter as tk
import time
from os.path import dirname,abspath
from pathlib import Path
import sys
import subprocess
import webbrowser
root = tk.Tk()
root.geometry("600x400")
root.title("Candlelight")
candleDir = dirname(abspath(__file__))
candleIco = tk.PhotoImage(file=candleDir+"\\files\\candle.png")
root.iconphoto(False,candleIco)
root.config(bg="#222222")

cef.Initialize()

aeae = True

window_info = cef.WindowInfo()
window_info.SetAsChild(root.winfo_id(),[0, 0, 600, 400])

apps = {
    "Candlelight":candleDir+"/candlelight.py",
    "ThemeBuilder":candleDir+"/apps/ThemeBuilder/ThemeBuilder.py",
    "Candlelight Update":candleDir+"/apps/CandleUpdate/Update.py",
    "Candlelight Distros":candleDir+"/apps/CandleBuild/CandleBuild.py",
    "GitHub - Candlelight":"https://github.com/nbitzz/candlelight",
    "GitHub - Addons":"https://github.com/nbitzz/candle-extra-packages",
}

def openApp(name):
    global aeae
    if (apps[name].startswith("https://")):
        webbrowser.open(apps[name])
    else:
        subprocess.Popen("{} \"{}\"".format(sys.executable,apps[name]))
        aeae=False

    
bindings = cef.JavascriptBindings()
bindings.SetProperty("openApp",openApp)
rk = []
for x in apps.keys():
    rk.append(x)
bindings.SetProperty("appsK",rk)

browser = cef.CreateBrowserSync(window_info,url="file://{}".format(dirname(abspath(__file__))+"/files/launcher.html"))
browser.SetJavascriptBindings(bindings)

while aeae:
    cef.MessageLoopWork()
    root.update()
    time.sleep(1/60)