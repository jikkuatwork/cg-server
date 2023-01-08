const EventSource = require("eventsource")
const fs = require("fs")

const data = "This is the data that you want to write to the file"

fs.writeFile("/path/to/file", data, error => {
  if (error) {
    console.error(error)
    return
  }
  console.log("The file has been saved!")
})

const eventSource = new EventSource("https://ntfy.sh/jj-cg-ask/sse")
eventSource.onmessage = e => {
  console.log(e.data)
}
