import json
import urllib.request

url = "https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json"

with urllib.request.urlopen(url) as response:
    data = json.load(response)

with open('euro.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)