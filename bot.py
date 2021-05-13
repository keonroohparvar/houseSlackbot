import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

mesage_counts = {}
choremessages = {}
userIds = {
    "Remy": "remywolf.r",
    "Blake": "blakethomas249",
    "Riley": "rsmith92",
    "Keon": "kroohpar",
    "Josh":"thanjosh2000",
    "Corey":"cagena65",
    "Dakota":"dakotaholling",
    "Mike":"mikee.kieran",
    "Carter":"cartergcromer",
    "Chris":"chriscunningham222222",
    "Max":"maxhallred",
    "Jeffrey":"jawexler"
}

class ChoreDirectMessage:
    START_TEXT = {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Welcome to this channel! \n\n'
                '*Get started by completing the tasks!*'
            )
        }
    }

    DIVIDER = {'type': 'divider'}

    def __init__(self, channel, user):
        self.channel = channel
        self.user = user
        self.icon_emoji = ':robot_face:'
        self.timestamp = ""
        self.chores = []
        self.completed = False
    
    def get_message(self):
        return {
            'ts': self.timestamp,
            'channel': self.channel,
            'username': 'Chore Bot',
            'icon_emoji': self.icon_emoji,
            'blocks': [
                self.START_TEXT,
                self.DIVIDER,
                self._get_reaction_task()
            ]

        }

    def _get_reaction_task(self):
        checkmark = ':white_check_mark:'
        if not self.completed:
            checkmark =':white_large_square:'
        
        text= f'{checkmark} *React to this message!*'

        return {'type': 'section', 'text': {'type': 'mrkdwn', 'text': text}}





def get_user_ids(channel):
    request = client.api_call("users.list")
    if request['ok']:
        for item in request['members']:
            print(item['name'])


def send_chore_message(channel, user):
    choreDM = ChoreDirectMessage(channel, user)
    message = choreDM.get_message()
    response = client.chat_postMessage(**message)
    choreDM.timestamp = response['ts']
    
    if channel not in choremessages:
        choremessages[channel] = {}
    choremessages[channel][user] = choreDM


# @slack_event_adapter.on('message')
# def message(payload):
#     event = payload.get('event', {})
#     channel_id = event.get('channel')
#     user_id = event.get('user')
#     text = event.get('text')
    
#     if user_id != None and BOT_ID != user_id:
#         if user_id in message_counts:
#             [user_id] += 1
#         else:
#             message_counts[user_id] = 1
        
#     if text.lower() == 'chores':
#         send_chore_message(channel_id, user_id)


if __name__ == '__main__':
    # send_chore_message("#chores", "Keon")
    # get_user_ids("test")
