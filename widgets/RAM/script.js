(container,options) => {
    let gugb = () => {
        let x = (JSON.parse(window.RAM).used/1000000000).toString()
        return x.split(".")[0]+"."+(x.split(".")[1] || "").slice(0,1)
    }    
    setInterval(() => {
        switch(options.display) {
            case "used":
                container.innerHTML = "RAM: "+gugb()+"GB used"
            break
            case "percent":
                container.innerHTML = "RAM: "+(JSON.parse(window.RAM).percent).toString()+"%"
            break
            case "used percent%":
                container.innerHTML = "RAM: "+gugb()+"GB "+(JSON.parse(window.RAM).percent).toString()+"%"
            break
        }
    },100)
    container.style["text-align"] = options.align
}