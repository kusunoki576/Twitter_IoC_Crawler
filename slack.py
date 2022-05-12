import requests
from slack_sdk import WebClient

from twitter import Tweet

SLACK_BOT_TOKEN = "YOUR TOKEN"



class SlackBot:
    def __init__(self) -> None:
        self.client = WebClient(token=SLACK_BOT_TOKEN)
        # self.client.chat_postMessage(channel="#general", text="==========Start processing==========")

    def send_start_message(self, username: str) -> None:
        pass
        # self.client.chat_postMessage(channel="#general", text=f"Checking {username}...")

    def send_detail_message(self, username: str, tweet: Tweet) -> None:
        self.client.chat_postMessage(channel="#general",\
            text=f"from https://twitter.com/{username}/status/{tweet.id}")
        self.client.chat_postMessage(channel="#general", text=f"```{tweet.text}```")
        self.client.chat_postMessage(channel="#general", text='Hashes: \r\n'+'\r\n'.join(tweet.hashes))
        self.client.chat_postMessage(channel="#general", text='Types: \r\n'+'\r\n'.join(tweet.virustotals))
        self.client.chat_postMessage(channel="#general", text="==============================")            