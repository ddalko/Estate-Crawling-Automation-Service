import requests
URL = 'https://www.aptgin.com/home/sub04/Sub0402PG.json?loc1=0000000000&nType=a&year=2020'
data = {'loc1': '0000000000',
        'nType': 'a',
        'year':'2020'}
res = requests.post(URL, data=data)
print(res.json())

