def write_to_file(text):
    with open('Resp.txt', 'w') as f:
        f.write(text)
    f.close()



'''
API = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'
updates = requests.get(API + 'getUpdates').json()
message = updates['result'][0]['message']['text']
'''