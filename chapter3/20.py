import json

file_list = open('jawiki-country.json').readlines()
for item in file_list:
    json_item = json.loads(item)
    if json_item['title'] == 'イギリス':
        print(json_item['text'])
        break

