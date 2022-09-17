#!/usr/bin/python3

import requests

mycoin = (0.03290706) #En orden: Binance, Huobi, Orionx 
investment = 1146 #Enter how much you spent total eg 'investment = 632'
url = "https://www.bitstamp.net/api/v2/ticker/btcusd/" #Replace "btcgbp" with your local fiat, supported values found here: https://www.bitstamp.net/api/
data = requests.get(url).json()
print('%s%s' % ("BTC:     ".ljust(13),data[u'last'].rjust(0)))
last = float(data['last'])
mycoinfiat = mycoin * last
net = mycoinfiat - investment
totalfiat = format(mycoinfiat, '.2f')
totalnet = format(net, '.2f')
#print("Mis bits:      " + totalfiat)
#print("Lost/Gain:          " + totalnet)