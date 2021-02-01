import requests
from pprint import pprint

def sendMsg(ids, text):
    payload = {
        'chat_id': ids,
        'text': text
    }
    token = '1623544581:AAGcmnpip3itggtxdUpX_GK7CdW-y1jmkic'
    url2 = f'https://api.telegram.org/bot{token}/sendMessage'
    r2 = requests.get(url2, params=payload)
    # pprint(r2.json())

def echo():
    token = '1623544581:AAGcmnpip3itggtxdUpX_GK7CdW-y1jmkic'
    url1 = f'https://api.telegram.org/bot{token}/getUpdates'
    r1 = requests.get(url1)
    # print(r1.json())
    data = r1.json()
    updates = data['result']

    # for update in updates:
        # message = update['message']
        # text = message['text']
        # user = message['from']
        # i = user['id']
        # print(i)
    for update in updates:
        message = update['message']
        text = message['text']
        user = message['from']
        i = user['id']
        sendMsg(i, text)
echo()

