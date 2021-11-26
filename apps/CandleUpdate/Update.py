from cefpython3 import cefpython as cef
import tkinter as tk
import time
from os.path import dirname,abspath
from pathlib import Path
import tkinter.filedialog
import hashlib
import json
import shutil
import math
import getpass
import hashlib
root = tk.Tk()
root.geometry("600x400")
root.title("Candlelight Update")
candleDir = dirname(dirname(dirname(abspath(__file__))))
candleIco = tk.PhotoImage(file=candleDir+"\\files\\candle.png")
root.iconphoto(False,candleIco)
cef.Initialize()


aeae = True
queueA = []

window_info = cef.WindowInfo()
window_info.SetAsChild(root.winfo_id(),[0, 0, 600, 400])


bindings = cef.JavascriptBindings()

browser = cef.CreateBrowserSync(window_info,url="file://{}".format(dirname(abspath(__file__))+"/update.html"))
browser.SetJavascriptBindings(bindings)

ptys = None

def screen(t,tx):
    browser.ExecuteJavascript("openAsErrorScreen(\"{}\",\"{}\")".format(t.replace("\"","\\\""),tx.replace("\"","\\\"")))

def updateCandleWith(nb):
    if (nb.exists()):
        if (nb/"files"/"candle").exists():
            tx = (nb/"files"/"candle").read_text()
            try:
                if (int(tx.split(",")[1]) > int(Path(candleDir+"/files/candle").read_text().split(",")[1])):
                    screen('Updating...',"This may take a few seconds. Please stand by.")
                    cef.MessageLoopWork()
                    root.update()
                    # This is going to be a mess but whatever
                    nSF = json.loads((nb/"settings.json").read_text())
                    oSF = json.loads(Path(candleDir+"/settings.json").read_text())
                    widgetReplacements = {}
                    widgetDNU = []
                    for x in (nb/"files"/"update.txt").read_text().split("\n"):
                        if (not x[0:1] == ";"):
                            args = x.split(' ')
                            cmd = args[0]
                            args.pop(0)
                            if (cmd=="del"):
                                widgetDNU.push(args[1])
                            elif cmd=="wrep":
                                widgetReplacements[args[1]] = args[2]
                    for x in (Path(candleDir)/"themes").glob('*'):
                        if not (Path(nb)/"themes"/x.name):
                            shutil.copyfile(x.resolve(),(Path(nb)/"themes"/x.name).resolve())
                    for x in (Path(candleDir)/"Packages").glob('*'):
                        if not (Path(nb)/"Packages"/x.name):
                            shutil.copytree(x.resolve(),(Path(nb)/"Packages"/x.name).resolve())
                    for x in (Path(candleDir)/"widgets").glob('*'):
                        if not (Path(nb)/"widgets"/x.name) and not x.name in widgetDNU:
                            shutil.copytree(x.resolve(),(Path(nb)/"widgets"/x.name).resolve())
                    for x in nSF.keys():
                        if x != "widgets":
                            nSF[x] = oSF[x]
                    for x in oSF["widgets"].keys():
                        if (oSF["widgets"][x]["name"]) in widgetReplacements:
                            nSF["widgets"][x] = {"name":widgetReplacements[oSF["widgets"][x].name],"settings":{}}
                        else:
                            nSF["widgets"][x] = oSF["widgets"][x]
                    (nb/"settings.json").write_text(json.dumps(nSF))
                    screen("Update successful","You can now use the new version of Candlelight.")


                else:
                    screen('Version outdated',"The version you selected is outdated.")
            except Exception as e:
                screen("An error occured","Restart Candlelight Update and try again.<br>{}".format(e))
            except SystemExit as e:
                screen("An error occured","Restart Candlelight Update and try again.<br>{}".format(e))
        else:
            screen('Invalid dir',"Please select a new version of Candlelight.")
    else:
        screen('Invalid dir',"Please select a new version of Candlelight.")

class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""
        if not is_loading:
            queueA.append(lambda: updateCandleWith(Path(tkinter.filedialog.askdirectory())))

browser.SetClientHandler(LoadHandler())

while aeae:
    cef.MessageLoopWork()
    root.update()
    time.sleep(1/60)
    for x in queueA:
        x()
    queueA = []