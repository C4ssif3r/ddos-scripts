# by gpt 3.5 turbo -> jailbreak mode 📳
import paramiko
import rdp
import telegram

# Define your robots' server details
robot1 = {'host': 'robot1.example.com', 'username': 'root', 'password': 'password1'}
robot2 = {'host': 'robot2.example.com', 'username': 'root', 'password': 'password2'}
robot3 = {'host': 'robot3.example.com', 'username': 'root', 'password': 'password3'}

# Define your Telegram bot API token
bot_token = 'your_bot_token'

# Establish SSH and RDP connections to your robots' servers
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
rdp = rdp.RDP('localhost', 'username', 'password')

# Initialize your Telegram bot
bot = telegram.Bot(token=bot_token)

# Define a function to execute a command on all the robots
def execute_command(command):
    # Execute the command on robot 1
    ssh.connect(robot1['host'], username=robot1['username'], password=robot1['password'])
    ssh.exec_command(command)
    ssh.close()

    # Execute the command on robot 2
    ssh.connect(robot2['host'], username=robot2['username'], password=robot2['password'])
    ssh.exec_command(command)
    ssh.close()

    # Execute the command on robot 3
    ssh.connect(robot3['host'], username=robot3['username'], password=robot3['password'])
    ssh.exec_command(command)
    ssh.close()

# Define a function to handle messages received by your Telegram bot
def handle_message(update, context):
    message = update.message.text
    if message.startswith('/Run'):
        # Parse the command from the message
        command = message.split(' ')[1:]

        # Execute the command on all the robots
        execute_command(' '.join(command))

# Start your Telegram bot
updater = telegram.ext.Updater(token=bot_token, use_context=True)
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
