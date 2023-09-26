import requests
import json

url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
r = requests.get(url)
respone = json.loads(r.text)
print(respone["text"])