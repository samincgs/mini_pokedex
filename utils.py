import requests
from config import POKEAPI_URL

def get_pokemon_data(pokemon):
    try:
        r = requests.get(POKEAPI_URL + pokemon)
    except:
        print('wrong type for parameter') 
        
    return r

def extract_pokemon_data(pokemon):
    data = {}
    p = get_pokemon_data(pokemon=pokemon).json()
    
    #pokemon name (still get from api even tho we have pokemon parameter since it can be a number)
    data['name'] = p['name']
    #pokemon types 
    data['types'] = p['types']
    # sprites
    data['sprite'] = p['sprites']['back_default']
    
    return data
            
            
    
    
    
    
        
    
