"""
Checking interesting or boring ints using
'Numbersapi' API
"""

import json
import requests

f = open('D:/dataset_24476_3.txt', 'r')

for line in f:
    api_url = "http://numbersapi.com/{}/math?json=true".format(line.rstrip())
    res = requests.get(api_url)
    data = res.json()
    if data['found'] is True:
        print('Interesting')
    else:
        print('Boring')

f.close()