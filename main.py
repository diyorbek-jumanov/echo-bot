import requests

token = '1686577699:AAESDP4XpohQfsAxWinHBVKtWwcJuDsrzhg'


def getUpdates():
    data = []
    url_Updates = f'https://api.telegram.org/bot{token}/getUpdates'
    res = requests.get(url_Updates)
    updates = res.json()['result']
    final_msg = updates[-1]
    up_id = final_msg['update_id']
    msg_text = final_msg['message']['text']
    chat_id = final_msg['message']['from']['id']
    data = [up_id, msg_text, chat_id]

    return data


def sendMessage(chatId, text):
    payload = {
        'chat_id': chatId,
        'text': text
    }
    url_sendMsg = f'https://api.telegram.org/bot{token}/sendMessage'
    r = requests.get(url_sendMsg, params=payload)
    
    return True


def echo_bot():
    data = getUpdates()
    final_update_id = data[0]
    
    while True:
        data = getUpdates()
        chatId = data[2]
        text = data[1]
        update_id = data[0]
        
        if final_update_id != update_id:
            sendMessage(chatId, text)
            final_update_id = update_id
        else:
            continue


echo_bot()
