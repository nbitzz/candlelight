window.commands.push({
    name:"js",
    action: function(arg) {
        open_in_notepad(eval(arg).toString())
    }
})
window.commands.push({
    name:"open",
    action: function(arg) {
        exec(`os.popen('${arg.replace(/\'/g,"\\'")}')`)
    }
})