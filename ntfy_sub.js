const fs = require("fs")
const EventSource = require("eventsource")
const dotenv = require("dotenv")

dotenv.config()

const SWAP_FILE = process.env.SWAP_FILE
const NTFY_ASK_TOKEN = process.env.NTFY_ASK_TOKEN

const formatToQuestion = query => {
  const request = JSON.parse(JSON.parse(query).message)

  switch (request.type) {
    case "explain":
      return `What are the main points of ${request.content}, using as minimal words as possible and avoiding repetition?`
    case "rewrite":
      return `Rewrite the following for better readability: ${request.content}`
    default:
      return "The default question!"
  }
}

const eventSource = new EventSource(`https://ntfy.sh/${NTFY_ASK_TOKEN}/sse`)
eventSource.onmessage = e => {
  const question = formatToQuestion(e.data)
  console.log(question)

  fs.writeFile(SWAP_FILE, question, error => {
    if (error) {
      console.error(error)
      return
    }
  })
}
