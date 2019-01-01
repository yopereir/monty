# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Update the account_sid and auth_token with the values from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Update the friendly_name and unique_name for the Assistant
assistant = client.autopilot \
                  .assistants \
                  .create(
                       friendly_name='UPDATE THIS VARIABLE',
                       unique_name='UPDATE_THIS_VARIABLE'
                   )

print(assistant.sid)

# Place assistant.sid here and DO NOT uncomment this line