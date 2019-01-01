# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Update the account_sid and auth_token with the values from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Replace 'variable' with the Task Action Variable for the task. Leave the 'task_actions' part at the end of the variable name (ex: assistant_greeting_task_actions)
# Replace the 'say' prompt with T
# Replace the value for 'listen' with False ONLY if the Assistant will not listen for a response
convert_string_to_integer_task_actions = {
    'actions': [
        {'say': '''You can convert a string to an integer by typing s, t, r which is short for string followed by two parentheses. You
        will place the integer inside the parentheses.'''},
        {'listen': True}
    ]
}


# Replace 'UAXXX...' with the assistant_sid https://www.twilio.com/console/autopilot/list
# Replace the 'unique_name' placeholder with the task's Unique Name
# Replace the 'actions' placeholder with the same value as the variable_task_actions used above
task = client.autopilot.assistants('UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                       .tasks \
                       .create(
                           unique_name='convert_string_to_integer',
                           actions=convert_string_to_integer_task_actions)

print("The task has been created!")
print(task.sid)