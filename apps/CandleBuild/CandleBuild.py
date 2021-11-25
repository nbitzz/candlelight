# Don't expect nice code in these apps, they're mostly for me or for creative people anyway
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
root = tk.Tk()
root.geometry("600x400")
root.title("Candlelight Distros")
candleDir = dirname(dirname(dirname(abspath(__file__))))
candleIco = tk.PhotoImage(file=candleDir+"\\files\\candle.png")
root.iconphoto(False,candleIco)

cef.Initialize()


aeae = True
queueA = []

window_info = cef.WindowInfo()
window_info.SetAsChild(root.winfo_id(),[0, 0, 600, 400])

def aml(name,content):
    global aeae
    Path(candleDir+"\\temp\\distro.zip".format(name)).write_text(content)
    aeae=False

packages = []
themes = []

for x in Path(candleDir+"/Packages").glob("*"):
    packages.append(x.name)

for x in Path(candleDir+"/themes").glob("*"):
    themes.append(x.name[0:len(x.name)-4])

def buildDistro(packagesEnabled,defaultTheme):
    global ptys
    nd = "C:\\Users\\{}\\Desktop\\{}".format(getpass.getuser(),"DISTROBUILD_TEMP"+str(math.floor(time.time())))
    
    for x in (Path(candleDir)/"temp").glob("*"):
        x.unlink()
    shutil.copytree(candleDir,nd)
    ndp = Path(nd)
    dfdt = json.loads(ptys.read_text())
    dfdt["pkg"] = json.loads(packagesEnabled)
    dfdt["theme"] = defaultTheme
    (ndp/"settings.json").write_text(json.dumps(dfdt))
    # Cleanup
    if (ndp/"default.json").exists():
        (ndp/"default.json").unlink()
    # Zip
    shutil.make_archive(candleDir+"\\temp\\candlelightDistro{}.zip".format(math.floor(time.time())),"zip",nd)
    browser.ExecuteJavascript("openAsErrorScreen('Distro build complete','Your distro has been built. Check the temp folder.')")

bindings = cef.JavascriptBindings()
bindings.SetProperty("finTheme",aml)
bindings.SetProperty("packageNames",json.dumps(packages))
bindings.SetProperty("themeNames",json.dumps(themes))
bindings.SetProperty("buildDistro",buildDistro)

browser = cef.CreateBrowserSync(window_info,url="file://{}".format(dirname(abspath(__file__))+"/builder.html"))
browser.SetJavascriptBindings(bindings)

ptys = None

def distroConfig(path):
    global ptys
    if (path.exists()):
        if json.loads(path.read_text()):
            ptys = path
            browser.ExecuteJavascript('document.getElementById("nScrn").style.display = "none";document.getElementById("cfgScrn").style.display = "block"')
        else:
            browser.ExecuteJavascript("openAsErrorScreen('Invalid file','Restart CandleBuild and try again.')")
    else:
        browser.ExecuteJavascript("openAsErrorScreen('Invalid file','Restart CandleBuild and try again.')")



class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""
        if not is_loading:
            bindings.SetProperty("packageNames",json.dumps(packages))
            bindings.Rebind()
            browser.ExecuteJavascript('loadCfgScreen()')
            if not Path(candleDir+"\\default.json").exists():
                print("no default")
                queueA.append(lambda: distroConfig(Path(tkinter.filedialog.askopenfile().name)))
            else:
                print("default")
                queueA.append(lambda: distroConfig(Path(candleDir+"\\default.json")))

browser.SetClientHandler(LoadHandler())

while aeae:
    cef.MessageLoopWork()
    root.update()
    time.sleep(1/60)
    for x in queueA:
        x()
    queueA = []
