try:
    import os
    from os.path import abspath, dirname
    import sys
    from pynput import keyboard
    from pynput.keyboard import Key
    from pynput.mouse import Controller as MouseController
    from pynput.mouse import Button as MouseButton
    import time
    from cefpython3 import cefpython as cef
    import pyautogui
    import tkinter as tk
    import webbrowser
    import json
    from pathlib import Path
    import math
    import getpass
    import psutil
    import platform
    import tkinter.messagebox as TkMessage
    import ctypes
    import itertools
    import string
except ImportError as e:
    import tkinter.messagebox
    import tkinter
    import sys
    from pathlib import Path
    import os
    import platform
    rt = tkinter.Tk()
    rt.attributes("-alpha",0)
    rt.overrideredirect(1)
    moduleName = str(e)[int(len("No module named'")+1):int(len(str(e))-1)]
    if platform.system() != "Windows":
        TkMessage.showerror("Unsupported","Candlelight does not support {}. Please use Windows instead.".format(platform.system()))
        exit()
    ae = tkinter.messagebox.askyesno("ImportError","An error occured while importing modules\n"+str(e)+"\nDo you want to install "+moduleName+"?",)
    if ae:
        if sys.executable:
            if (Path(sys.executable).parent/"Scripts"/"pip.exe").exists:
                
                print("{} install {}".format((Path(sys.executable).parent/"Scripts"/"pip.exe").resolve(),moduleName))
                os.popen("{} install {}".format((Path(sys.executable).parent/"Scripts"/"pip.exe").resolve(),moduleName))
                tkinter.messagebox.showinfo("Information","Candlelight is now attempting to install this module.\nIf the installation fails, run the command found in the console.")
            else:
                tkinter.messagebox.showerror("No pip.exe","pip.exe was not found. Unable to install.")
        else:
            tkinter.messagebox.showerror("No interpreter","No interpreter found. Try again later.")
            rt.destroy()
            exit()
    else:
        rt.destroy()
        exit()

Mouse = MouseController()

root = tk.Tk()
root.overrideredirect(1)
root.geometry("520x50")
root.attributes("-alpha",0)
root.attributes("-topmost",True)
candleIco = tk.PhotoImage(file=dirname(abspath(__file__))+"\\files\\candle.png")
root.iconphoto(False,candleIco)
root.config(bg="#222222")


if platform.system() != "Windows":
    TkMessage.showerror("Unsupported","Candlelight does not support {}. Please use Windows instead.".format(platform.system()))
    exit()

def get_available_drives(): # i got lazy lol, here's something that i just stole. oh well, i'll probably learn what it's doing soon
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    return list(itertools.compress(string.ascii_uppercase,
               map(lambda x:ord(x) - ord('0'), bin(drive_bitmask)[:1:-1])))
#https://stackoverflow.com/questions/4188326/in-python-how-do-i-check-if-a-drive-exists-w-o-throwing-an-error-for-removable

root.wm_attributes('-transparentcolor', '#666666')

CefFrame = tk.Frame(root,width=520,height=50)
CefFrame.grid(sticky="NSWE",row=0,column=1)

def changeToProperSizing(xL,pos):
    x = 60
    properX = (pyautogui.size()[0]/2)-260
    properY = (pyautogui.size()[1]/2)-x/2
    newYSize = int((pyautogui.size()[1]/2))
    if (pos == "top"):
        properY = 20
        newYSize = pyautogui.size()[1]-20
    root.geometry("520x{}".format(newYSize))
    CefFrame.config(height=newYSize)
    root.geometry("+{}+{}".format(int(properX),int(properY)))
    root.update()
    oldMP = Mouse.position
    Mouse.position = (int(properX+20),int(properY+20))
    Mouse.press(MouseButton.left)
    Mouse.release(MouseButton.left)
    Mouse.position = oldMP

def properFocus():
    if cndOpen:
        queueA.append(root.focus)
        queueA.append(lambda: browser.SetFocus(True))
        queueA.append(lambda: browser.ExecuteJavascript("searchBar.focus()"))

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'
    

window_info = cef.WindowInfo()
window_info.SetAsChild(CefFrame.winfo_id(),[0, 0, 520, pyautogui.size()[1]])
bindings = cef.JavascriptBindings(
            bindToFrames=False, bindToPopups=False)
def properReload():
    widgetNames = []
    themeNames = []
    packages = []
    sjs = Path(dirname(abspath(__file__))+"/settings.json").read_text()
    for x in Path(dirname(abspath(__file__))+"/widgets").glob("*"):
        widgetNames.append({
            "name":x.name,
            "script":(x/'script.js').read_text(),
            "data":json.loads((x/'data.json').read_text()),
        })
    # geuss it's not spagehaeha
    for x in Path(dirname(abspath(__file__))+"/Packages").glob("*"):
        packages.append({
            "name":x.name,
            "js":(x/"package.js").read_text()
        })
        if x.name in json.loads(sjs)["pkg"] and (x/"python.py").exists():
            exec((x/"python.py").read_text())
    for x in Path(dirname(abspath(__file__))+"/themes").glob("*"):
        themeNames.append(x.name[0:len(x.name)-4])
    bindings.SetProperty("USERNAME",getpass.getuser())
    bindings.SetProperty("widgets",json.dumps(widgetNames))
    bindings.SetProperty("themes",json.dumps(themeNames))
    bindings.SetProperty("candleVersionFile",Path(dirname(abspath(__file__))+"/files/candle").read_text())
    bindings.SetProperty("CustomTheme",Path(dirname(abspath(__file__))+"/themes/"+json.loads(sjs)["theme"]+".css").read_text())
    bindings.SetProperty("setting",sjs)
    bindings.SetProperty("packages",json.dumps(packages))
    bindings.SetProperty("DIR",dirname(abspath(__file__)))
    browser.Reload()
    bindings.Rebind()

cndOpen = False    

def tellUpdateFile():
    if tk.messagebox.askyesno("New update","A new version seems to be available.\nWould you like to go to the GitHub Releases page?"):
        webbrowser.open("https://github.com/nbitzz/candlelight/releases")
        if cndOpen:
            Candlelight()

def saveSettings(x):
    Path(dirname(abspath(__file__))+"/settings.json").write_text(x)

def open_in_notepad(txt):
    newF = Path(dirname(abspath(__file__))+"/temp/"+str(math.floor(time.time()*1000))+".txt")
    newF.write_text(txt)
    os.popen("C:\\Windows\\system32\\notepad.exe {}".format(newF.resolve()))

PLYN = True

def exfnc():
    global PLYN
    PLYN = False

bindings.SetFunction("sizing",changeToProperSizing)
bindings.SetFunction("properFocus",properFocus)
bindings.SetFunction("exec",exec)
bindings.SetFunction("exit",exfnc)
bindings.SetFunction("reloadBrowser",properReload)
bindings.SetFunction("saveSettings",saveSettings)
bindings.SetFunction("open_in_notepad",open_in_notepad)
bindings.SetFunction("tellNewerVersion",tellUpdateFile)

cef.Initialize({},{"use-fake-ui-for-media-stream":True,"enable-media-stream":True,"disable-web-security":True})
browser = cef.CreateBrowserSync(window_info,url="file://{}".format(dirname(abspath(__file__))+"/candle_int.html"))
browser.SetJavascriptBindings(bindings)
properReload()

queueA = []



oldMousePos = (0,0)

def get_disk_info(diskLetter):
    dk = diskLetter+":"
    if Path(dk).exists():
        bindings.SetProperty("disk_{}".format(diskLetter),json.dumps({"percentage":psutil.disk_usage(dk).percent,"full":psutil.disk_usage(dk).free+psutil.disk_usage(dk).used,"used":psutil.disk_usage(dk).used}))
    else:
        bindings.SetProperty("disk_{}".format(diskLetter),json.dumps({"display":"Disk not found"}))
    bindings.Rebind()

def Candlelight():
    bindings.Rebind()
    global cndOpen
    cndOpen = not cndOpen
    if cndOpen: 
        queueA.append(lambda: root.attributes("-alpha",1))
        queueA.append(lambda: browser.SetFocus(True))
        queueA.append(lambda: root.focus())
        #queueA.append(lambda: browser.ExecuteJavascript("setTimeout(() => {searchBar.focus()},1000)"))
        queueA.append(lambda: browser.ExecuteJavascript("returnToNormalMenu()"))
        queueA.append(lambda: root.deiconify())
        for x in get_available_drives():
            get_disk_info(x)
        sjs = json.loads(Path(dirname(abspath(__file__))+"/settings.json").read_text())
        queueA.append(lambda: changeToProperSizing(70,sjs["ui_put"]))
        
    else:
        queueA.append(lambda: root.attributes("-alpha",0))

bindings.SetFunction("candle",Candlelight)

def candleCheck(e):
    sjs = json.loads(Path(dirname(abspath(__file__))+"/settings.json").read_text())
    if (str(e) == "Key."+sjs["hotkey"]):
        Candlelight()

listener = keyboard.Listener(
    on_release=candleCheck)
listener.start()

lastPFTime = 0

while PLYN:
    time.sleep(1/60)
    root.update()
    cef.MessageLoopWork()
    for x in queueA:
        x()
    queueA = []
    if (time.time()-lastPFTime >= 1):
        bindings.SetProperty("CPU_USAGE",psutil.cpu_percent())
        ramData = psutil.virtual_memory()
        bindings.SetProperty("RAM",json.dumps({"percent":ramData.percent,"used":ramData.used}))
        lastPFTime = time.time()
        bindings.Rebind()
