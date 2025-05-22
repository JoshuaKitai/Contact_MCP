from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

load_dotenv()

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def send_slack_message(channel: str, message: str):
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message
        )
        print(f"Message sent to {channel}: {response['message']['text']}")
        return response
    except SlackApiError as e:
        print(f"Slack API error: {e.response['error']}")
        return None
