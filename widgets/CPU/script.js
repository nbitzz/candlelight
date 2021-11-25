(container,options) => {
    
    setInterval(() => {
     container.innerHTML = "CPU "+window.CPU_USAGE.toString()+"%"   
    },1000)
    container.style["text-align"] = options.align
}