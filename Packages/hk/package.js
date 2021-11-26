window.commands.push({
    name:"hk",
    action: function(arg) {
        let x = arg.split(" ")
        switch(x[0]) {
            case "click":
                exec(`
Candlelight()
for x in range(${x[1] || 50}):
    Mouse.press(MouseButton.left)
    Mouse.release(MouseButton.left)
                `)
            break
            case "rightclick":
                exec(`
Candlelight()
for x in range(${x[1] || 50}):
    Mouse.press(MouseButton.right)
    Mouse.release(MouseButton.right)
                `)
            break
            case "butterfly":
                exec(`
Candlelight()
for x in range(${x[1] || 50}):
    Mouse.press(MouseButton.left)
    Mouse.release(MouseButton.left)
    Mouse.press(MouseButton.right)
    Mouse.release(MouseButton.right)
                `)
            break

        }
    },
    autocomplete: [
        {
            name:"click",
            autocomplete: [
                {
                    name:'50'
                },
                {
                    name:'100'
                },
                {
                    name:'250'
                },
                {
                    name:'500'
                }
            ]
        },
        {
            name:"rightclick",
            autocomplete: [
                {
                    name:'50'
                },
                {
                    name:'100'
                },
                {
                    name:'250'
                },
                {
                    name:'500'
                }
            ]
        },
        {
            name:"butterfly",
            autocomplete: [
                {
                    name:'50'
                },
                {
                    name:'100'
                },
                {
                    name:'250'
                },
                {
                    name:'500'
                }
            ]
        }
    ]
})