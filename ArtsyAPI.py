import json
import requests

client_id = 'ea90cf7a9a38e22263f4'
client_secret = 'ea80ff8331dc64f58a08cdf2ce816a5d'

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
    r = requests.get("https://api.artsy.net/api/artists/{}".format(line), headers=headers)
    r.encoding = 'utf-8'
    # server answer
    j = json.loads(r.text)
    print(j)
    try:
        dict_artist[j['sortable_name']] = j['birthday']
    except KeyError:
        pass
print(dict_artist)
f.close()