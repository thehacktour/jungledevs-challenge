import requests
import json
from requests.auth import HTTPBasicAuth

url = "https://api.sportsdata.io/v3/mma/odds/json/EventOdds/52"

headers = {'Accept': 'application/json'}
auth = HTTPBasicAuth('apikey', 'ac433c72064f4ccfb64d9ec0ce995a99')

resultado = requests.get(url, headers=headers,  auth=auth)

print(resultado.text)
print(resultado.status_code)
