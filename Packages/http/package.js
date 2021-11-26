window.commands.push({
    name:"http",
    action: function(arg) {
        let args = arg.split(" ")
        let orq = new XMLHttpRequest()
        switch(args[0].toLowerCase()) {
            case "get":
                
                orq.open("GET",args[1] || "https://example.com")
                orq.send()
                orq.onload = function() {
                open_in_notepad(orq.responseText)
                }
                window.candle()
            break
            case "post":
                orq.open("POST",args[1] || "https://example.com")
                orq.send(args.slice(2).join(" "))
                orq.onload = function() {
                open_in_notepad(orq.responseText)
                }
            break
            /*
            case "postjson":
                let orq = new XMLHttpRequest()
                orq.open("GET",args[1] || "https://example.com")
                orq.send(args.slice(1).join(" "))
                orq.onload = function() {
                open_in_notepad(orq.responseText)
                }
            break
            */
        }
    },
    autocomplete: [
        {
            name:"get",
        },
        {
            name:"post"
        }/*,
        {
            name:"postJSON"
        }*/
    ]
})