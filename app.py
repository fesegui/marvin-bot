"""Example of a Facebook Messenger Bot
"""

import os
import json

from flask import Flask, request
from messenger import MessengerClient
from messenger.content_types import TextMessage


FACEBOOK_VERIFICATION_TOKEN = os.environ.get('FACEBOOK_VERIFICATION_TOKEN')
FACEBOOK_PAGE_TOKEN = os.environ.get('FACEBOOK_PAGE_TOKEN')

app = Flask(__name__)
client = MessengerClient(FACEBOOK_PAGE_TOKEN)


@app.route('/', methods=['GET'])
def handle_verification():
    print('Handling Verification.')
    if request.args.get('hub.verify_token', '') == FACEBOOK_VERIFICATION_TOKEN:
        print('Verification successful!')
        return request.args.get('hub.challenge', '')

    print('Verification failed!')
    return 'Error, wrong validation token'


@app.route('/', methods=['POST'])
def handle_messages():
    message_entries = json.loads(request.data.decode('utf8'))['entry']
    for entry in message_entries:
        for message in entry['messaging']:
            if message.get('message'):
                print('[INFO] message:', message)
                sender_id = message['sender']['id']
                text = message['message']['text']
                client.send(sender_id, text)
    return 'OK'

if __name__ == '__main__':
    app.run()
