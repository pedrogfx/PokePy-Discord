import requests
import json

args = input("Put a Pokemon name => ")  #pokemon name

pokeName = args.lower()

try:
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokeName}')
    packages_json = r.json()
    packages_json.keys()
        

    print(packages_json['name'])
    print(packages_json['order'])
    print(packages_json['sprites']['back_default'])
    print(packages_json['weight'])
    print(packages_json['height'])
    for type in packages_json['types']:
        print(type['type']['name'])
    print('Pokemon Bot - Python')
except:
    print("Pokemon not found!")