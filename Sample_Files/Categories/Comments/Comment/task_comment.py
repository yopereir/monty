# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Replace the account_sid and auth_token with the values from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Replace 'variable' with the Task Action Variable for the task. Leave the 'task_actions' part at the end of the variable name (ex: assistant_greeting_task_actions)
# Replace the 'say' prompt with T
# Replace the value for 'listen' with False ONLY if the Assistant will not listen for a response
comment_task_actions = {
    'actions': [
        {'say': '''Comments can be used for various reasons. You can use comments to withhold blocks of code from executing.
        You can also use comments as a reference in your code to help another programmer understand your code better. To use a
        comment, use the hash character and type your comment directly to the right. If you want to extend your comment to the another
        line, you\'ll need to either use a hash on the next line or use a multi-line comment.'''},
        {'listen': True}
    ]
}


# Replace 'UAXXX...' with the assistant_sid https://www.twilio.com/console/autopilot/list
# Replace the 'unique_name' placeholder with the task's Unique Name
# Replace the 'actions' placeholder with the same value as the variable_task_actions used above
task = client.autopilot.assistants('UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                       .tasks \
                       .create(
                           unique_name='comment',
                           actions=comment_task_actions)

print("The task has been created!")
print(task.sid)