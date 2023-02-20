import requests


def best_hero(heroes: list):
    heroes_dict = {}
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    hero_info = requests.get(
        url)
    if hero_info.status_code != 200:
        return "Error"
    hero_js = hero_info.json()
    for hero_name in hero_js:
        h_name = hero_name['name']
        if h_name in heroes:
            heroes_dict[h_name] = int(hero_name['powerstats']['intelligence'])
    top_hero = max(heroes_dict, key=lambda x: heroes_dict[x])
    result = f"\nСамый умный супергерой: {top_hero} - его интелект: {heroes_dict[top_hero]}"
    return result


print(best_hero(['Thanos', 'Hulk', 'Captain America']))
