# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Update the account_sid and auth_token with the values from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Replace 'variable' with the Task Action Variable for the task. Leave the 'task_actions' part at the end of the variable name (ex: assistant_greeting_task_actions)
# Replace the 'say' prompt with T
# Replace the value for 'listen' with False ONLY if the Assistant will not listen for a response
execute_python_code_task_actions = {
    'actions': [
        {'say': '''Before you execute your Python code, you\'ll need to ensure that the file extension is dot py. After
        you\'ve confirmed that the file extension is correct, you will need to open the terminal and navigate to the location
        of your Python file. Once you\'re in the correct directory, type the word Python space and then the file name and press enter.
        If your code contains no errors, then your Python code will execute.'''},
        {'listen': True}
    ]
}


# Replace 'UAXXX...' with the assistant_sid https://www.twilio.com/console/autopilot/list
# Replace the 'unique_name' placeholder with the task's Unique Name
# Replace the 'actions' placeholder with the same value as the variable_task_actions used above
task = client.autopilot.assistants('UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                       .tasks \
                       .create(
                           unique_name='execute_python_code',
                           actions=execute_python_code_task_actions)

print("The task has been created!")
print(task.sid)