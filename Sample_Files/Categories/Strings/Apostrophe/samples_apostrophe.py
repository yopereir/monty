# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Update the account_sid and auth_token with the values from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Replace the 'phrases' placeholders with your Samples for the task (minimum 10)
phrases = [
    'Write an apostrophe in Python',
    'Use an apostrophe',
    'Apostrophe',
    'Write apostrophe',
    'Use apostrophe'
    'Use apostrophe in a string'
]

# Replace 'UAXXX...' with the assistant_sid https://www.twilio.com/console/autopilot/list
# Replace the 'tasks' placeholder with the Unique Name for the task
for phrase in phrases:
    sample = client.autopilot \
        .assistants('UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
        .tasks('apostrophe') \
        .samples \
        .create(language='en-us', tagged_text=phrase)

    print(sample.sid)