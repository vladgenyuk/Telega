import requests
import os.path


save_path = "/cards\\"
complete_path = os.path.join(save_path + 'cards.txt' )
r = requests.get('https://www.deckofcardsapi.com/api/deck/new/draw/?count=52').json()

with open(complete_path, 'w') as x:
    x.write('Список всех карт')
x.close()

for i in r['cards']:
    with open(complete_path, 'a') as image:
        image.write(i['value'] + '-' + i['suit'] + '\n')
    image.close()




