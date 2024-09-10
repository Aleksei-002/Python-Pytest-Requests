import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c837388fdf9c9f3b259e769a9e8e037d'
HEADER =  {'Content-Type' : 'application/json'}

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', headers= HEADER)
    assert response.status_code == 200

def test_my_trainers():
    response_my_trainers = requests.get(url=f'{URL}/trainers', headers= HEADER, params ={'trainer_id': 6431})
    assert response_my_trainers.json()["data"][0]["id"]=='6431'


