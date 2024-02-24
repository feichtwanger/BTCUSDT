import requests
import pyglet
import schedule
from config import API_KEY

symbol = 'BTCUSDT'
api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

def price():
    if response.status_code == requests.codes.ok:

        data = response.json()
        price = data['price']
        symbol = data['symbol']
    #print(data['price'])
        p2 = float(price)
        print(f'{p2}$')
        print(symbol)
    
        if p2 < 51520.00:
            sound = pyglet.media.load('audio.mp3')
            sound.play()
            pyglet.app.run()
        else:
            print('Price is high than 51520\n')
    else:
        print("Error:", response.status_code, response.text)

def main():
    #price()

    schedule.every(30).minutes.do(price)
    
    while True:
        schedule.run_pending()
    
if __name__ == '__main__':
    main()
    


