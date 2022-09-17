#!/usr/bin/python3

import requests

mycoin = 1.75848 #Enter how much BTC you own here, eg 'mycoin = 0.267567823'
investment = 200 #Enter how much you spent total eg 'investment = 632'
url = "https://api.binance.com/api/v1/ticker/price?symbol=ETCUSDT" #
data = requests.get(url).json()
#print('%s%s' % ("CAKE:".ljust(13),data[u'price'].rjust(0)))
last = float(data['price'])
mycoinfiat = mycoin * last
net = mycoinfiat - investment
totalfiat = format(mycoinfiat, '.2f')
totalnet = format(net, '.2f')
valor = format(last, '.2f')
print("ETC:           " + valor)
print("Mis ETCs:       " + totalfiat)
#print("Lost/Gain:     " + totalnet)