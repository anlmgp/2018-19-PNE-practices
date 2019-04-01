import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = ["/jokes/count", '/categories', '/jokes/random']
METHOD = "GET"

headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)

for i in ENDPOINT:
    conn.request(METHOD, i, None, headers)
    r1 = conn.getresponse()
    text_json = r1.read().decode("utf-8")
    conn.close()
    # -- Generate the object from the json file
    data = json.loads(text_json)
    if i == "/jokes/count":
        number = data['value']
    elif i == '/categories':
        name = data['value']
        number1 = len(name)
    elif i == '/jokes/random':
        j = data['value']
        joke = j['joke']

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

print("The number of jokes avaiables of Chuck Norris is {}.".format(number))
print("The name of categories is {} and {}, and the number of categories is {}.".format(name[0],name[1],number1))
print('A random joke: {}'.format(joke))