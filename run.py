import os
import time
import requests
from pyChatGPT import ChatGPT
from dotenv import load_dotenv

load_dotenv()

ntfy_token = os.environ["NTFY_TOKEN"]
swap_file = os.environ["SWAP_FILE"]
answer_file = os.environ["ANSWER_FILE"]
email = os.environ["OAI_EMAIL"]
password = os.environ["OAI_PASSWORD"]

def setup():
    open(swap_file, "a").close()
    return ChatGPT(auth_type='openai', email=email, password=password)

api = setup()

print("Ready.")

def send_as_file(answer):
    file = open(answer_file, "w")
    file.write(answer)

def send_as_notification(message):
    requests.get("https://ntfy.sh/{token}/publish?message={m}&priority=high&tags=robot".format(m=message, token=ntfy_token))

def read_and_clear(file):
    file = open(file, "r+")
    content = file.read()
    file.truncate(0)
    file.close()
    return content.strip()

while True:
    topic = read_and_clear(swap_file).rstrip()
    if not topic:
        time.sleep(1)
        continue
    print("Querying: {t}".format(t=topic))
    response = api.send_message(topic)
    print(response['message'])
    send_as_notification((response['message']))
    send_as_file((response['message']))
