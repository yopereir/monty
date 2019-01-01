# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Replace the account_sid and auth_token with the values from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Update the friendly_name and unique_name for the Assistant
assistant = client.autopilot \
                  .assistants \
                  .create(
                       friendly_name='Monty',
                       unique_name='monty'
                   )

print(assistant.sid)

# Place assistant.sid here and DO NOT uncomment this line