# Linked Lists

#class Pokemon:
#    def __init__(self, name, types):
#        self.name = name
#        self.types = types
#        self.is_caught = False  
#my_pokemon = Pokemon(name='Pikachu', types=['Electric'])


class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):  # or use __str__(self)
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })


    def catch(self):
	    self.is_caught = True
    

    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")
    
    def add_type(self, new_type):
	    self.types.append(new_type)
         
def get_by_type(my_pokemon, pokemon_type):
    have_type = []
    for p in my_pokemon:
        if pokemon_type in Pokemon.types:
            have_type.append(p)
    return have_type
		
#quirtle = Pokemon("Squirtle", ["Water"])
#quirtle.is_caught = True
#quirtle.print_pokemon()

#my_pokemon = Pokemon("rattata", ["Normal"])
#my_pokemon.print_pokemon()
#
#my_pokemon.catch()
#my_pokemon.print_pokemon()
#

#my_pokemon = Pokemon("rattata", ["Normal"])
#my_pokemon.print_pokemon()
#
#my_pokemon.choose()
#my_pokemon.catch()
#my_pokemon.choose()

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()



