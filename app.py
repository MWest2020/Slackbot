# import requests
# import pytz
# import os
# from datetime import datetime, timedelta

# def is_dst_active():
#     local_timezone = pytz.timezone("Europe/Amsterdam")
#     now = datetime.now(local_timezone)
#     return now.dst() != timedelta(0)

# def send_slack_message(token, channel, message):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {token}'
#     }
    
#     payload = {
#         'channel': channel,
#         'text': message
#     }
    
#     response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, json=payload)
    
#     if response.status_code != 200:
#         raise ValueError(f"Request to Slack API failed: {response.status_code}, {response.text}")

# if __name__ == "__main__":
#     local_timezone = pytz.timezone("Europe/Amsterdam")
#     current_time = datetime.now(local_timezone).time()

#     target_time = datetime.strptime("16:30", "%H:%M").time()

#     if current_time.hour == target_time.hour and current_time.minute == target_time.minute:
#         SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")  # Fetch from environment variables
#         CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")    # Channel ID where the message should be posted
#         MESSAGE = ":rotating_light:ISSUES + UREN. Tot over 10 min.:rotating_light:"

#         send_slack_message(SLACK_API_TOKEN, CHANNEL_ID, MESSAGE)


import requests
import os

def send_slack_message(token, channel, message):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    payload = {
        'channel': channel,
        'text': message
    }
    
    response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, json=payload)
    
    if response.status_code != 200:
        raise ValueError(f"Request to Slack API failed: {response.status_code}, {response.text}")

    # Log the response for debugging
    print(f"Slack API response: {response.json()}")

if __name__ == "__main__":
    SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")  # Fetch from environment variables
    CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")  # Channel ID where the message should be posted
    MESSAGE = ":rotating_light:ISSUES, UREN & REPORT OUT gedaan? Indien vergeten, wil je dat aub nog doen?.:rotating_light:"

    # Print the variables for debugging (excluding the token for security)
    print(f"Channel ID: {CHANNEL_ID}")
    
    send_slack_message(SLACK_API_TOKEN, CHANNEL_ID, MESSAGE)
