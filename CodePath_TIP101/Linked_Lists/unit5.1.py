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

    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            have_type.append(pokemon)

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

#jigglypuff = Pokemon("Jigglypuff", ["Normal"])
#jigglypuff.print_pokemon()
#
#jigglypuff.add_type("Fairy")
#jigglypuff.print_pokemon()
#
# initializing pokemons
#jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
#diglett = Pokemon("Diglett", ["Ground"])
#meowth = Pokemon("Meowth", ["Normal"])
#pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
#blastoise = Pokemon("Blastoise", ["Water"])
#
#my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
#normal_pokemon = get_by_type(my_pokemon, "Normal")
#print(normal_pokemon)


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
          
def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.value)
        current = current.next
    print(" -> ".join(values))

node_one = Node('a')
node_two = Node('b')
node_one.next = node_two
l = ["Mario", "Luigi", "Wario", "Toad"]
node_1 = Node("Mario")
node_2 = Node("Luigi")
node_3 = Node("Wario")
node_4 = Node("Toad")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

    
#print(node_one.value) 
#print(node_one.next) 
#print(node_two.value)
#print(node_two.next) 


#print(node_one.value)
#print(node_one.next.value)
#print(node_two.value)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

#
#Mario -> Luigi
#Luigi -> Wario
#Wario -> Toad
#Toad -> None
#

    
    


# Create and link nodes
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.next = b
b.next = c
c.next = d
d.next = e
# input linked list: a->b->c->d->e
print_linked_list(a)


#--------------------- Problem Set Version 2 -------------------------------------
#                            (Below)


#--------------------- Problem Set Version 3 -------------------------------------
#                            (Below)
