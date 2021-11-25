# This is a mess lol, oh well.
# Yeah I recommend you just edit the CSS files but this should work
from cefpython3 import cefpython as cef
import tkinter as tk
import time
from os.path import dirname,abspath
from pathlib import Path
root = tk.Tk()
root.geometry("600x400")
root.title("Candlelight ThemeBuilder")
candleDir = dirname(dirname(dirname(abspath(__file__))))
candleIco = tk.PhotoImage(file=candleDir+"\\files\\candle.png")
root.iconphoto(False,candleIco)

cef.Initialize()

aeae = True

window_info = cef.WindowInfo()
window_info.SetAsChild(root.winfo_id(),[0, 0, 600, 400])

def aml(name,content):
    global aeae
    Path(candleDir+"\\themes\\{}.css".format(name)).write_text(content)
    aeae=False

bindings = cef.JavascriptBindings()
bindings.SetProperty("finTheme",aml)

browser = cef.CreateBrowserSync(window_info,url="file://{}".format(dirname(abspath(__file__))+"/builder.html"))
browser.SetJavascriptBindings(bindings)

while aeae:
    cef.MessageLoopWork()
    root.update()
    time.sleep(1/60)