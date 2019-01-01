# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Update the account_sid and auth_token with the values from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Replace 'variable' with the Task Action Variable for the task. Leave the 'task_actions' part at the end of the variable name (ex: assistant_greeting_task_actions)
# Replace the 'say' prompt with T
# Replace the value for 'listen' with False ONLY if the Assistant will not listen for a response
apostrophe_task_actions = {
    'actions': [
        {'say': '''Since single quotes are used when creating a string, you will need to use an escape key to use an
        apostrophe. To use an apostrophe in a string, you first type a backslash followed by a single quote and then the rest of the
        word. Therefore, if you\'re typing the word I'm, you would type the letter I, backlash, single quote, then the letter M altogether
        with no spaces.'''},
        {'listen': True}
    ]
}


# Replace 'UAXXX...' with the assistant_sid https://www.twilio.com/console/autopilot/list
# Replace the 'unique_name' placeholder with the task's Unique Name
# Replace the 'actions' placeholder with the same value as the variable_task_actions used above
task = client.autopilot.assistants('UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                       .tasks \
                       .create(
                           unique_name='apostrophe',
                           actions=apostrophe_task_actions)

print("The task has been created!")
print(task.sid)