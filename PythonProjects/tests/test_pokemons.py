import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
token='e0263d1d5e4f922ea054625117b9e9f2'
header={'Content-Type':'application/json', 'trainer_token': token}
trainer_id='13359'

def test_status_code():
    response=requests.get(url=f'{URL}/pokemons', params={'trainer_id':trainer_id})
    assert response.status_code==200

def test_part_of_response():
    response_get=requests.get(url=f'{URL}/pokemons', params={'trainer_id':trainer_id})
    assert response_get.json()["data"][0]["name"]== 'Бульбазавр'

@pytest.mark.parametrize('key,value',[('name', 'Бульбазавр'),('trainer_id', trainer_id),('id', '187614')])
def test_parametrize(key,value):
    response_parametrize=requests.get(url=f'{URL}/pokemons', params={'trainer_id':trainer_id})
    assert response_parametrize.json()["data"][0][key]== valuef