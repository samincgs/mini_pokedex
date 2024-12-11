import requests
from io import BytesIO
from PIL import Image
from requests.exceptions import JSONDecodeError
from .config import POKEAPI_URL

def get_pokemon_data(pokemon):
    try:
        r = requests.get(POKEAPI_URL + pokemon)
    except JSONDecodeError():
        r = None
        
    return r

def extract_pokemon_data(pokemon):
    p = get_pokemon_data(pokemon=pokemon)
    data = {}
    
    if p:
        p = p.json()
        #pokemon name (still get from api even tho we have pokemon parameter since it can be a number)
        data.update({'name' : p['name'], 
                     'types': p['types'], 
                     'sprite': p['sprites']['front_default'], 
                     'abilities': p['abilities'],
                     'moves': p['moves'],
                     'height': p['height'],
                     'weight': p['weight']
                     })
        # data['name'] = p['name']
        
        # #pokemon types 
        # data['types'] = p['types']
        
        # # sprites
        # data['sprite'] = p['sprites']['front_default']
        
        # #abilities
        # data['abilities'] = p['abilities']
    
    return data
                        
def convert_into_photo(url, size=(200, 200)):
    res = requests.get(url)
    res.raise_for_status()
    
    image = BytesIO(res.content)
    img = Image.open(image).resize(size)
    
    return img
    
    
    
        
    
