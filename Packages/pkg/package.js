window.commands.push({
    name:"pkg",
    action: function(arg) {
        let args = arg.split(" ")
        switch(args[0]) {
            case "toggle":
                if (JSON.parse(window.packages).find(e => e.name == args[1])) {
                    if (args[1] != "pkg") {
                        let st = JSON.parse(window.setting)
                        if (st.pkg.findIndex(e => e == args[1]) > -1) {
                            st.pkg.splice(st.pkg.findIndex(e => e == args[1]),1)
                            window.saveSettings(JSON.stringify(st))
                            window.reloadBrowser()
                        } else {
                            st.pkg.push(args[1])
                            window.saveSettings(JSON.stringify(st))
                            window.reloadBrowser()
                        }
                    } else {
                        createCustomMenu({value:"Are you sure you want to disable pkg?",disabled:true},[
                            {name:"Yes",action:function() {
                                let st = JSON.parse(window.setting)
                                st.pkg.splice(st.pkg.findIndex(e => e == "pkg"),1)
                                window.saveSettings(JSON.stringify(st))
                                window.reloadBrowser()
                            }},
                            {name:"No",action:returnToNormalMenu}
                        ]) 
                    }
                }
            break
            case "use":
                if (st.pkg.findIndex(e => e == args[1]) < -1) {
                    st.pkg.push(args[1])
                    window.saveSettings(JSON.stringify(st))
                    window.reloadBrowser()
                }
            break
            case "enabled":
                let em = JSON.parse(window.setting).pkg
                let enabledModulesT = []
                em.forEach((v,x) => {
                    enabledModulesT.push({
                        text:true,
                        name:v,
                        action:()=>{}
                    })
                })
                createCustomMenu({value:"Enabled packages",disabled:true},[
                    ...enabledModulesT,
                    {name:"OK",action:returnToNormalMenu}
                ])
            break
        }
    },
    autocomplete: [
        {
            name:"toggle",
            autocomplete:JSON.parse(window.packages)
        },
        {
            name:"enabled"
        }
    ]
})