import requests
from pprint import pprint

def get_data(link):
    link = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    result_js = link.json()
    return result_js

def find_name(link, names_list):
    info = get_data(link)
    h_names = []
    h_stat = []
    for i in info:
        for name in names_list:
            if i['name'] == name:
                h_names.append(i['name'])
                h_stat.append(i['powerstats']['intelligence'])
    hero_intel = zip(h_names, h_stat)
    compare_dict = dict(hero_intel)
    result = max(compare_dict.items())
    pprint(f'Highest intelligence belongs to {result}')

data = 'https://akabab.github.io/superhero-api/api/all.json'
get_data(data)
names = ['Thanos', 'Hulk', 'Captain America']
find_name(data, names)
