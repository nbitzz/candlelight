(container,options) => {
    let pn = () => {
        let oreq = new XMLHttpRequest()
        oreq.open("GET",options.site)
        let time = Date.now()
        oreq.send()
        oreq.onload = function() {
            let png = Date.now()-time
            let ae = {true:"#44FF44",false:"rgba(255,255,255,0.5)"}
            let scores = `<span style="color:${ae[png < 1000]}">*</span><span style="color:${ae[png < 750]}">*</span><span style="color:${ae[png < 500]}">*</span><span style="color:${ae[png < 250]}">*</span>`
            container.innerHTML = `${scores} ${png}ms`
        }
    }
    setInterval(pn,parseInt(options.ping_every,10))
    pn()
    container.style["text-align"] = options.align
}