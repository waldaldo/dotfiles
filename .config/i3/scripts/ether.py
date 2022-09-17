#!/usr/bin/python3

import requests

mycoin = 0.3620376 #Enter how much you own here, eg 'mycoin = 0.267567823'
investment = 861 #Enter how much you spent total eg 'investment = 632'
url = "https://www.bitstamp.net/api/v2/ticker/ethusd/" #Replace "btcgbp" with your local fiat, supported values found here: https://www.bitstamp.net/api/
data = requests.get(url).json()
print('%s%s' % ("ETH: ".ljust(14),data[u'last'].rjust(0)))
last = float(data['last'])
mycoinfiat = mycoin * last
net = mycoinfiat - investment
totalfiat = format(mycoinfiat, '.2f')
totalnet = format(net, '.2f')
#print("Mis eth:       " + totalfiat)
print("Lost/Gain:       " + totalnet)
