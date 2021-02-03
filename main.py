import requests
from pprint import pprint

token = '1686577699:AAESDP4XpohQfsAxWinHBVKtWwcJuDsrzhg'


def getUpdates():
    data = []
    url_Updates = f'https://api.telegram.org/bot{token}/getUpdates'
    res = requests.get(url_Updates)
    updates = res.json()['result']
    # pprint(updates)
    final_msg = updates[-1]
    up_id = final_msg['update_id']
    msg_text = final_msg['message'].get('text')
    sticker = final_msg['message'].get('sticker')
    chat_id = final_msg['message']['from']['id']
    data = [up_id, msg_text, chat_id, sticker]
    
    return data


def sendMessage(chatId, text):
    payload = {
        'chat_id': chatId,
        'text': text,
    }
    url_sendMsg = f'https://api.telegram.org/bot{token}/sendMessage'
    r = requests.get(url=url_sendMsg, params=payload)
    # print(r.url)


def sendSticker(chatId, stker):
    payload = {
        'chat_id': chatId,
        'sticker': stker,
    }
    url_sendMsg = f'https://api.telegram.org/bot{token}/sendSticker'
    r = requests.get(url=url_sendMsg, params=payload)
    print(r.url)
    

def echo_bot():
    final_update_id = 0
    while True:
        data = getUpdates()
        # pprint(data)
        stkr = data[3]
        chatId = data[2]
        text = data[1]
        update_id = data[0]
        if final_update_id != update_id:
            if text != None:
                sendMessage(chatId, text)
            else:
                sendSticker(chatId, stkr)
            final_update_id = update_id


echo_bot()
