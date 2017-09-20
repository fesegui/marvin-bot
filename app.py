"""Example of a Facebook Messenger Bot
"""

import os
import json

from flask import Flask, request
from messenger import MessengerClient
from messenger.content_types import TextMessage
from bot import Bot


FACEBOOK_PAGE_TOKEN = os.environ.get('FACEBOOK_PAGE_TOKEN')
FACEBOOK_VERIFICATION_TOKEN = os.environ.get('FACEBOOK_VERIFICATION_TOKEN')
PRESENTATION_URL = os.environ.get('PRESENTATION_URL', 'https://www.google.com.br/')
PRESENTATION_MESSAGE = 'E aí, cara! Eu sou o Marvin! Tô te mandando o link da palestra que ' + \
                       'tá rolando agora. Acessa aí :D'

app = Flask(__name__)
bot = Bot()
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
            sender_id = message['sender']['id']
            if message.get('message'):
                print('[INFO] message:', message)
                text = message['message']['text']
                reply = bot.reply(sender_id, text)
                print('[INFO] reply:', reply)
                client.send(sender_id, TextMessage(reply))
            elif message.get('postback'):
                if message['postback'].get('referral'):
                    if message['postback']['referral']['ref'] == 'palestra-bots':
                        print('[INFO] message:', message['postback']['referral']['ref'])
                        print('[INFO] reply:', PRESENTATION_MESSAGE + '\n' + PRESENTATION_URL)
                        client.send(sender_id, TextMessage(PRESENTATION_MESSAGE))
                        client.send(sender_id, TextMessage(PRESENTATION_URL))
            elif message.get('referral'):
                if message['referral']['ref'] == 'palestra-bots':
                    print('[INFO] message:', message['referral']['ref'])
                    print('[INFO] reply:', PRESENTATION_MESSAGE + '\n' + PRESENTATION_URL)
                    client.send(sender_id, TextMessage(PRESENTATION_MESSAGE))
                    client.send(sender_id, TextMessage(PRESENTATION_URL))
    return 'OK'

if __name__ == '__main__':
    app.run()
