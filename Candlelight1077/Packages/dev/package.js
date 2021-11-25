window.commands.push({
    name:"dev",
    action: function(arg) {
        let x = arg.split(" ")
        switch(x[0]) {
            case "tools":
                exec("browser.ShowDevTools()")
                searchBar.value = ''
            break
            case "enable_other_focus":
                searchBar.onblur = undefined;
                searchBar.value = ''
            break
            case "enable_context_menu":
                document.oncontextmenu = undefined;
                searchBar.value = ''
            break
            case "reload":
                reloadBrowser()
            break
            case "quit_next_loop":
                exit()
            break

        }
    },
    autocomplete: [
        {
            name:"tools"
        },
        {
            name:"enable_other_focus"
        },
        {
            name:"enable_context_menu"
        },
        {
            name:"reload"
        },
        {
            name:"quit_next_loop"
        }
    ]
})