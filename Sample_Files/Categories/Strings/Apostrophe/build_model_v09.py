# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Update the account_sid and auth_token with the values from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Replace 'UAXXX...' with the assistant_sid https://www.twilio.com/console/autopilot/list
# Replace the 'unique_name' version number with the appropriate version number for the build
model_build = client.autopilot \
                    .assistants('UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                    .model_builds \
                    .create(unique_name='v0.9')

print(model_build.sid)