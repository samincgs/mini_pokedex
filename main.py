import customtkinter as ctk
from PIL import Image, ImageTk

from scripts.config import *
from scripts.utils import extract_pokemon_data, convert_into_photo

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Mini Pokedex')
        self.geometry(str(SCREEN_WIDTH) + 'x' + str(SCREEN_HEIGHT))
        self.resizable(False, False)
        
        self.pokemon_choice = ctk.StringVar(self, 'charmander')
        self.current_pokemon = None
        
        self.entry = ctk.CTkEntry(self, placeholder_text='text', textvariable=self.pokemon_choice)
        self.entry.pack()
        
        self.submit_button = ctk.CTkButton(self,text='submit', command=self.update_pokemon)
        self.submit_button.pack()
        
        self.img_label = ctk.CTkLabel(self, text='')
        self.img_label.pack()
        
        self.update_pokemon()
    
    def update_pokemon(self):
        if self.current_pokemon != self.pokemon_choice.get():
            self.data = extract_pokemon_data(self.pokemon_choice.get())
            if self.data:
                self.current_pokemon = self.pokemon_choice.get()
                self.poke_img = ctk.CTkImage(convert_into_photo(self.data['sprite']), size=(200, 200))
                self.img_label.configure(image=self.poke_img, text ='')
            else:
                self.current_pokemon = None
                self.img_label.configure(image='', text='')
                 
           
        
        
if __name__ == '__main__':
    app = App()
    app.mainloop()
    