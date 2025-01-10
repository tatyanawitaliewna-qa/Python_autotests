import requests

URL='https://api.pokemonbattle.ru/v2'
token='e0263d1d5e4f922ea054625117b9e9f2'
header={'Content-Type':'application/json', 'trainer_token': token}

body_registration= {
    "trainer_token":token,
    "email": "tatyanawitaliewna@yandex.u",
    "password": "Asd123KLwe"
}

body_confirmation= {
    "trainer_token":token
}

body_create={
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change={
    "pokemon_id": "187880",
    "name": "New Name",
    "photo_id": 2
}

body_catch={
    "pokemon_id": "187888"
}


'''response=requests.post(url=f'{URL}',headers=header, json=body_registration)
print(response.text)'''

'''response_confirmation=requests.post(url=f'{URL}/trainers/confirm_email',headers=header, json=body_confirmation)
print(response_confirmation.text)'''

response_create=requests.post(url=f'{URL}/pokemons',headers=header, json=body_create)
print(response_create.text)
message=response_create.json()['message']
print(message)

response_change=requests.put(url=f'{URL}/pokemons',headers=header, json=body_change)
print(response_change.text)
message=response_change.json()['message']
print(message)

response_catch=requests.post(url=f'{URL}/trainers/add_pokeball',headers=header, json=body_catch)
print(response_catch.text)
message=response_create.json()['message']
print(message)