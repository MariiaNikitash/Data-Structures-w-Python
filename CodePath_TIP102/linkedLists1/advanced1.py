# OPP and LL 
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        #self.personality = personality
        #self.neighbor = neighbor
        self.furniture = []


    def add_item(self, item_name):
        if item_name in ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]:
            self.furniture.append(item_name)

# 3, 4
def of_personality_type(townies, personality_type):
    pass

def message_received(start_villager, target_villager):
    pass


apollo = Villager("Apollo", "Eagle", "pah")
#print(apollo.name)
#print(apollo.species) 
#print(apollo.catchphrase)
#print(apollo.furniture)

# P 5
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

# Add code here to link the above nodes
#print(print_linked_list(kk_slider))

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    current = head
    while current:
        print(f"I cought a {head.fish_name} ")


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None



#print_linked_list(fish_list)
#print_linked_list(catch_fish(fish_list))
#print(catch_fish(empty_list))

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    pass







# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def restock(head, new_fish):
    current = head
    while current:
        current = current.next
    current.next = new_fish

    return head
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))