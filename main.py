import customtkinter as ctk
from PIL import Image, ImageTk

from scripts.config import *
from scripts.utils import extract_pokemon_data

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Pokemon Finder')
        self.geometry(str(SCREEN_WIDTH) + 'x' + str(SCREEN_HEIGHT))
        self.resizable(False, False)
        
        self.data = extract_pokemon_data('charmander')
        
        
        
        
        
if __name__ == '__main__':
    app = App()
    app.mainloop()