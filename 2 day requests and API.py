import requests 

access_key = 'your_key'

headers = {
    'X-Yandex-Weather-Key': access_key
}

response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=52.37125&lon=4.89388', headers=headers)
if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)