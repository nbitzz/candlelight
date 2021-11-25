(container,options) => {
    let writeAs = ""
    if (options.styling != "None") {
        writeAs = `${options.styling}, `
    }
    container.innerHTML = writeAs+window.USERNAME
    container.style["text-align"] = options.align
}