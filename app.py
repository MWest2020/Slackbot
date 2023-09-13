import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Set up the Slack client
slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

def post_message_to_general():
    try:
        # Call the chat.postMessage method using the WebClient
        response = client.chat_postMessage(channel='#general', text=":rotating_light:ISSUES + UREN. Tot over 10 min.:rotating_light:")
        
        # Validate if the message was sent successfully
        assert response["message"]["text"] == ":rotating_light:ISSUES + UREN. Tot over 10 min.:rotating_light:"
    except SlackApiError as e:
        # error message indicates with two lights. 
        print(f":rotating_light::rotating_light:ISSUES + UREN. Tot over 10 min.:rotating_light:")

# Call the function
post_message_to_general()
