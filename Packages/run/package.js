window.commands.push({
    name:"js",
    action: function(arg) {
        open_in_notepad(eval(arg).toString())
    }
})