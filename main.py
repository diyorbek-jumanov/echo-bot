import requests
from pprint import pprint

token = '1686577699:AAESDP4XpohQfsAxWinHBVKtWwcJuDsrzhg'


def getUpdates():
    data = []
    url_Updates = f'https://api.telegram.org/bot{token}/getUpdates'
    res = requests.get(url_Updates)
    updates = res.json()['result']
    final_msg = updates[-1]
    pprint(final_msg)
    up_id = final_msg['update_id']
    msg_id = final_msg['message']['message_id']
    msg_text = final_msg['message'].get('text')
    sticker = final_msg['message'].get('sticker')
    if sticker != None:
        sticker = sticker['file_id']
    chat_id = final_msg['message']['from']['id']
    data = [up_id, msg_text, chat_id, sticker, msg_id]
    
    return data


def sendMessage(chatId, text, m_d):
    payload = {
        'chat_id': chatId,
        'text': text,
        'reply_to_message_id': m_d
    }
    url_sendMsg = f'https://api.telegram.org/bot{token}/sendMessage'
    r = requests.get(url=url_sendMsg, params=payload)
    # print(r.url)


def sendSticker(chatId, stker, reply_to_message_id):
    payload = {
        'chat_id': chatId,
        'sticker': stker,
        'reply_to_message_id': reply_to_message_id
    }
    url_sendstkr = f'https://api.telegram.org/bot{token}/sendSticker'
    r = requests.get(url=url_sendstkr, params=payload)
    # print(r.json())
    

def echo_bot():
    final_update_id = 0
    while True:
        data = getUpdates()
        # pprint(data)
        m_id = data[4]
        stkr = data[3]
        chatId = data[2]
        text = data[1]
        update_id = data[0]
        if final_update_id != update_id:
            if text != None:
                sendMessage(chatId, text, m_id)
            else:
                sendSticker(chatId, stkr, m_id)
            final_update_id = update_id
            


echo_bot()
