import requests
from io import BytesIO
from PIL import Image, ImageTk
from requests.exceptions import JSONDecodeError
from .config import POKEAPI_URL

def get_pokemon_data(pokemon):
    try:
        r = requests.get(POKEAPI_URL + pokemon)
    except JSONDecodeError():
        r = False
        
    return r

def extract_pokemon_data(pokemon):
    p = get_pokemon_data(pokemon=pokemon)
    data = {}
    
    if p:
        p = p.json()
        #pokemon name (still get from api even tho we have pokemon parameter since it can be a number)
        data['name'] = p['name']
        
        #pokemon types 
        data['types'] = p['types']
        
        # sprites
        data['sprite'] = p['sprites']['front_default']
        
        #abilities
        data['abilities'] = p['abilities']
    
    return data
            
            
def convert_into_photo(url):
    res = requests.get(url)
    res.raise_for_status()
    
    image = BytesIO(res.content)
    img = Image.open(image).resize((200, 200))
    # poke_img = ImageTk.PhotoImage(img)
    
    return img
    
    
    
        
    
