"""
Program are checking the artist name for ID using Artsy API
"""

import json
import requests

client_id = '...'     #hidden
client_secret = '...' #hidden

# take the token
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                data={
                    "client_id": client_id,
                    "client_secret": client_secret
                })

# check the server answer
j = json.loads(r.text)
# return the token
token = j["token"]

dict_artist = {}
f = open("C:/Users/admin/.vscode/database.txt", "r")

for line in f:
    linestr = line.rstrip('\n')
    # create header with our token
    headers = {"X-Xapp-Token" : token}
    # init request with header
    r = requests.get("https://api.artsy.net/api/artists/{}".format(linestr), headers=headers)
    r.encoding = 'utf-8'
    # server response
    j = json.loads(r.text)
    try:
        dict_artist[j['sortable_name']] = j['birthday']
    except KeyError:
        pass
f.close()

dict_sorted = sorted(dict_artist.items(), key=lambda x: (x[1], x[0]))
for i in range(len(dict_sorted)):
    print(dict_sorted[i][0])
