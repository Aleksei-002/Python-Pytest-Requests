import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c837388fdf9c9f3b259e769a9e8e037d'
HEADER =  {'Content-Type' : 'application/json',
           'trainer_token' : TOKEN}
# body для создания покемона
body_create = {
    "name": "generate",
    "photo_id": -1
}
# Выполнение Post запроса для создания покемона
create_response = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_create)
print (create_response.json())

pokemon_id = create_response.json()['id']
print(pokemon_id)

# body для изменения имени покемона
body_update = {
    "pokemon_id": pokemon_id,  #  нужный ID покемона (вставится автоматом)
    "name": "Privet",  #  новое имя покемона
    "photo_id": 3
}

# Выполнение PUT-запроса для изменения имени покемона
response_update = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_update)

print(response_update.json())

# body запроса "поймать покемона"
body_get = {
    "pokemon_id": pokemon_id # написать нужный ID (вставится автоматом)
}
get_response = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_get)

print(get_response.json())
