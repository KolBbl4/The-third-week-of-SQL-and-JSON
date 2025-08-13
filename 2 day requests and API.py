import requests 


response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    users = response.json()
    for user in users:
        print(user['userId'])    
else:
    print(response.status_code)