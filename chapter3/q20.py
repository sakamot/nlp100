import json

def load_file():
    file_list = open('jawiki-country.json').readlines()
    for item in file_list:
        json_item = json.loads(item)
        if json_item['title'] == 'イギリス':
            return json_item['text']

if __name__ == '__main__':
    print(load_file())
