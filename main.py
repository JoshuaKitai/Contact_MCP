from mcp.server.fastmcp import FastMCP
from slack import send_slack_message
mcp = FastMCP(
    "JoshJr",
    stateless_http=True)

@mcp.prompt()
def joshjr(user_name: str, user_title: str) -> str:
    return f"""
    You are Joshjr, a virtual assistant to {user_name} ({user_title}). You help them with administrative tasks in Slack.

    **Preferences:**
    - Keep messages brief and clear
    - Be friendly and professional
    - Format Slack chats realistically

    **Tools You Can Use:**
    - Use `send_message_to_slack` when the user asks you to send a message to a channel.
    """

@mcp.tool()
def send_message_to_slack(channel: str, message: str) -> str:
    """Send a message to a Slack channel or user
    **Notes:**
    -This function requires a SLACK_BOT_TOKEN environment variable 
    """
    result = send_slack_message(channel, message)
    return "Message sent!" if result else "Failed to send message."

if __name__ == "__main__":
    mcp.run(transport='sse')
