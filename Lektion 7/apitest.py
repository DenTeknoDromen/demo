import requests
import json

url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm"
r = requests.get(url)
response_string = r.text
respone_dictionary = json.loads(r.text)
print(respone_dictionary)
