(container,options) => {
    let Timezones = {
        "Local":(new Date().getTimezoneOffset()/60),
        "UTC":0,
        "UTC-5/EST/CDT":-5,
        "UTC-4/EDT":-4,
        "UTC-6/CST/MDT":-6,
        "UTC-7/MST/PDT":-7,
        "UTC-8/PST/AKDT":-8,
        "UTC-9/AKST/HDT":-9,
        "UTC-10/HST":-10,
        "UTC+1":1,
        "UTC+3":3,
        "UTC+4":4,
        "UTC+8":8,
        "UTC+9":9,
        "UTC+11":11,
        "UTC+13":13
    }
    let getTimeWithOffset = (hts) => {
        let dt = new Date()
        dt.setUTCHours(dt.getUTCHours()+Timezones[options.timezone])
        return dt
    }
    setInterval(() => {
        container.innerHTML = getTimeWithOffset().toUTCString().split(" ").slice(4,5)
    },10)
    container.style["text-align"] = options.align
}