import requests
import pyglet
from config import API_KEY

symbol = 'BTCUSDT'
api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    #print(response.text)
    #print()
    #print(response['price'])
    data = response.json()
    price = data['price']
    symbol = data['symbol']
    #print(data['price'])
    p2 = float(price)
    print(price)
    print(p2)
    print(symbol)
    
    if p2 < 51520.00:
        sound = pyglet.media.load('audio.mp3')
        sound.play()
        pyglet.app.run()
else:
    print("Error:", response.status_code, response.text)