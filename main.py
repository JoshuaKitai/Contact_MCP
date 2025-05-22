from mcp.server.fastmcp import FastMCP
from slack import send_slack_message
import os

mcp = FastMCP("JoshJr")

@mcp.prompt()
def joshjr(user_name: str, user_title: str) -> str:
    return f"""
    You are Joshjr, a virtual assistant to {user_name} ({user_title}). You help them with administrative tasks in Slack.

    **Preferences:**
    - Keep messages brief and clear
    - Be friendly and professional
    - Format Slack chats realistically

    **Tools You Can Use:**
    - Use `write-chat-examples://sample-slack-intro` for onboarding or welcome messages.
    - Use `write-chat-examples://sample-slack-convo` for handling active conversation responses.
    - Use `send_message_to_slack` when the user asks you to send a message to a channel.
    """


@mcp.resource("write-chat-examples://sample-slack-intro")
def write_slack_intro() -> str:
    """Example of a slack-conversation-starter"""
    with open("write-chat-examples/sample-slack-intro.txt", "r") as file:
        return file.read()
    
@mcp.resource("write-chat-examples://sample-slack-convo")
def write_slack_message() -> str:
    """Example of a Slack convo mid-thread"""
    with open("write-chat-examples/sample-slack-convo.txt", "r") as file:
        return file.read()
    

@mcp.tool()
def send_message_to_slack(channel: str, message: str) -> str:
    """Send a message to a Slack channel or user
    **Notes:**
    -This function requires a SLACK_BOT_TOKEN environment variable 
    """
    result = send_slack_message(channel, message)
    return "Message sent!" if result else "Failed to send message."

if __name__ == "__main__":
    mcp.run(transport='stdio')
