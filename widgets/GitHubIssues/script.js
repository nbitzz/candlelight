(container,options) => {
    let getGHData = () => {
        let rq = new XMLHttpRequest()
        console.log(options)
        rq.open("GET",`https://api.github.com/repos/${options.repo}`)
        rq.send()
        rq.onload = function() {
            container.innerHTML = `<img height="16" width="16" style="vertical-align:top;" src="file://${DIR}\\files\\GitHub-Mark-Light-32px.png"> Issues: ${JSON.parse(rq.responseText).open_issues_count}`
        }
    }
    setInterval(getGHData,parseInt(options.refresh_every,10))
    getGHData()
    container.style["text-align"] = options.align
}