(container,options) => {
    let getGHData = () => {
        let rq = new XMLHttpRequest()
        console.log(options)
        rq.open("GET",`https://api.github.com/repos/${options.repo}/releases`)
        rq.send()
        rq.onload = function() {
            container.innerHTML = `<img height="16" width="16" style="vertical-align:top;" src="file://${DIR}\\files\\GitHub-Mark-Light-32px.png">&nbsp;${(JSON.parse(rq.responseText)[0] || {tag_name:"??"}).tag_name}`
        }
    }
    container.style["white-space"] = "pre"
    setInterval(getGHData,parseInt(options.refresh_every,10))
    getGHData()
    container.style["text-align"] = options.align
}