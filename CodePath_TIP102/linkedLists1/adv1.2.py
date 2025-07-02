class Player:
    def __init__(self, character, kart, items=[]):
        self.character = character
        self.kart = kart
        self.items = items

player_one = Player("Yoshi", "Super Blooper")
#print(player_one.character)
#print(player_one.kart) 
#print(player_one.items)



class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def increment_rank(head, target):
    current = head
    prev = None


racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1)) 
print_linked_list(increment_rank(None, 1)) 
