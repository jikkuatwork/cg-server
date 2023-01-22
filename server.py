import os
from pyChatGPT import ChatGPT
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

ntfy_token = os.environ["NTFY_TOKEN"]
swap_file = os.environ["SWAP_FILE"]
email = os.environ["OAI_EMAIL"]
password = os.environ["OAI_PASSWORD"]

def setup():
    open(swap_file, "a").close()
    return ChatGPT(auth_type='openai', email=email, password=password)

api = setup()
print("Ready.")

app = FastAPI()

@app.get("/ask")
def ask(question: str):
    print("Querying: {t}".format(t=question))
    response = api.send_message(question)
    answer = response["message"]
    print(answer)
    return {"answer": answer, "conversation_id": "some-random-id"}
