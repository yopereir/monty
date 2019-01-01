# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Update the account_sid and auth_token with the values from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Replace 'UAXXX...' with the assistant_sid https://www.twilio.com/console/autopilot/list
# Here is the defaults directory. Replace the values for 'assistant_initiation' and 'fallback'
defaults = client.autopilot \
                 .assistants('UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                 .defaults() \
                 .update(defaults={
                      'defaults': {
                          'assistant_initiation': 'task://assistant_greeting',
                          'fallback': 'task://assistant_fallback'
                      }
                  })

print(defaults.assistant_sid)
