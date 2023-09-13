import requests
import json

# 13.1
# indata = 0
# while indata < 1:
#     indata = input("Ange ett positivt heltal: ")
#     try:
#         indata = int(indata)
#     except ValueError:
#         continue

# url = ("https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?"
#        f"integer={indata}")
# r = requests.get(url)
# response = json.loads(r.text)
# iseven = "udda"
# isprime = "inte"
# if response["even"]:
#     iseven = "jämnt"
# if response["prime"]:
#     isprime = ""
# strfactors = f'{response["factors"]}'.strip("[]")


# print(f'{response["integer"]} är ett {iseven} nummer. Det är {isprime} ett '
#       'primtal')
# print(f'Numrets faktorer är: {strfactors}')

# 13.2
# cities = ["Stockholm", "Göteborg", "Malmö", "Uppsala", "Västerås"]
# msg = (f"Välj en stad för att få väderprognos ifrån: {cities[0]}\n{cities[1]}"
#        f"\n{cities[2]}\n{cities[3]}\n{cities[4]}")

# while True:
#     print(msg)
#     indata = input(": ")
#     if indata in cities:
#         break
#     else:
#         msg = ("Välj en stad i listan")

# indata = indata.replace("å", "a")
# indata = indata.replace("ä", "a")
# indata = indata.replace("ö", "o")
# indata = indata.casefold()

# url = ("https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"
#        f"{indata}")
# r = requests.get(url)
# response = json.loads(r.text)
# forecasts = response["forecasts"]

# for x in forecasts:
#     print(f'{x["date"]}: {x["forecast"]}')

# 13.3
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

r = requests.get(url)
response = json.loads(r.text)
localartist = {}
for x in response["artists"]:
    print(x["name"])
    localartist[x["name"]] = x["id"]

print("----------------------------")
indata = input("Select artist: ")
print("----------------------------")

a = requests.get(url + localartist[indata])
response = json.loads(a.text)
artist = response["artist"]
genres = f'{artist["genres"]}'.strip("[]")
genres = genres.replace("'", "")
members = f'{artist["members"]}'.strip("[]")
members = members.replace("'", "")

print(f'Name: {artist["name"]}')
print(f'Genres: {genres}')
print(f'Years active: {artist["years_active"][0]}')
print(f'Member: {members}')
print("----------------------------")
