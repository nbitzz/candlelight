window.commands.push({
    name:"util",
    action: function(arg) {
        let x = arg.split(" ")
        switch(x[0]) {
            case "colorpick":
                exec(`
im = pyautogui.screenshot(region=(pyautogui.position()[0],pyautogui.position()[1],1,1))
cll = im.getpixel((0,0))
browser.ExecuteJavascript("searchBar.value = '{}'".format(rgbtohex(cll[0],cll[1],cll[2]).upper()))  
                `)
            break
            case "cursor":
                exec(`browser.ExecuteJavascript("searchBar.value = '{},{}'".format(pyautogui.position()[0],pyautogui.position()[1]))`)
            break
            case "screen":
                exec(`browser.ExecuteJavascript("searchBar.value = '{},{}'".format(pyautogui.size()[0],pyautogui.size()[1]))`)
            break

        }
    },
    autocomplete: [
        {
            name:"colorpick"
        },
        {
            name:"cursor"
        },
        {
            name:"screen"
        }
    ]
})