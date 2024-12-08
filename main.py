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
        
        self.type_label = ctk.CTkLabel(self, text='')
        self.type_label.pack()
        
        self.ability_label = ctk.CTkLabel(self, text='')
        self.ability_label.pack()
        
        self.update_pokemon()
    
    def not_found(self):
        self.current_pokemon = None
        self.ability_label.forget()
        self.img_label.forget()
        self.type_label.forget()
    
    def update_pokemon(self):
        if self.current_pokemon != self.pokemon_choice.get():
            self.data = extract_pokemon_data(self.pokemon_choice.get())
            if self.data:
                self.current_pokemon = self.pokemon_choice.get()
                self.update_image()
                self.update_type()
                self.update_ability()
            else:
                self.not_found()
    
    def update_image(self):
        self.poke_img = ctk.CTkImage(convert_into_photo(self.data['sprite']), size=(200, 200))
        self.img_label.configure(image=self.poke_img, text ='')
        self.img_label.pack()
        
    def update_ability(self):
        for ability in self.data['abilities']:
            self.ability_label.configure(text=f'{ability['ability']['name']}')
            self.ability_label.pack()
            
    def update_type(self):
        types = ''
        for p_type in self.data['types']:
            types += p_type['type']['name'] + '\t'
        
        self.type_label.configure(text=types)
        self.type_label.pack()
        
   
if __name__ == '__main__':
    app = App()
    app.mainloop()
    