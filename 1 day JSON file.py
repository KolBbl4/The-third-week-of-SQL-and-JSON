import json 

stirnJSON = '{"name": "Иван", "age": 30}' 
data = json.loads(stirnJSON) 

with open('exemple.json', 'r') as file:  
    loadJSON = json.load(file)
    print(loadJSON['links']['self'])

with open('data.json', 'w', encoding='utf-8') as file:  
    json.dump(data, file, ensure_ascii=False, indent=4) 