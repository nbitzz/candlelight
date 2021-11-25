(container,options) => {
    
    setInterval(() => {
        let diskdata = JSON.parse(window["disk_"+(options.disk.toUpperCase() || "C")] || JSON.stringify({display:`No disk ${options.disk.toUpperCase()}`})) 
        if (diskdata.display) {
            container.innerHTML = diskdata.display
        } else {
        switch(options.display) {
            case "used/full+percentage%":
                container.innerHTML = `${Math.floor(diskdata.used/1000000000)}/${Math.floor(diskdata.full/1000000000)}gb ${diskdata.percentage}%`
            break
            case "percentage":
                container.innerHTML = `Disk ${options.disk.toUpperCase() || "C"}: ${diskdata.percentage}%`
            break
            case "used/full":
                container.innerHTML = `${Math.floor(diskdata.used/1000000000)}/${Math.floor(diskdata.full/1000000000)}gb`
            break
            case "space_left":
                container.innerHTML = `${Math.floor((diskdata.full-diskdata.used)/1000000000)}gb left`
            break
        }
    }
    },1000)
    container.style["text-align"] = options.align
}