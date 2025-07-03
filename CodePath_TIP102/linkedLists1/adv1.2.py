class Player:
    def __init__(self, character, kart, items=[]):
        self.character = character
        self.kart = kart
        self.items = items

player_one = Player("Yoshi", "Super Blooper")
#print(player_one.character)
#print(player_one.kart) 
#print(player_one.items)

# -------------------------------------------------

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def add_item(self, item_name):
        valid_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
        if item_name in valid_items:
            self.items.append(item_name)


player_one = Player("Yoshi", "Dolphin Dasher")
#print(player_one.items)
player_one.add_item("red shell")
#print(player_one.items)
player_one.add_item("super star")
#print(player_one.items)
player_one.add_item("super smash")
#print(player_one.items)


def print_results(race_results):
    for place, racer in enumerate(race_results, start=1):
        print(f"{place}. {racer.character}")

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

#print_results(race_one)

#______________
class Player:
    def __init__(self, character, kart, ahead=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = ahead

def get_place(my_player):
    rank = 1
    cur = my_player
    while cur.ahead:
        rank+=1
        cur = cur.ahead
    return rank



peach = Player("Peach", "Daytripper") # 3
mario = Player("Mario", "Standard Kart M", peach) # 1
luigi = Player("Luigi", "Super Blooper", mario) #2

player1_rank = get_place(luigi)
player2_rank = get_place(peach)
player3_rank = get_place(mario)

#print(player1_rank)
#print(player2_rank)
#print(player3_rank)


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

daisy = Node("Daisy")
peach = Node("Peach")
luigi = Node("Luigi")
mario = Node("Mario")

daisy.next = peach 
peach.next = luigi
luigi.next = mario

print_linked_list(daisy)
#Daisy -> Peach -> Luigi -> Mario

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

def count_racers(head):
    count = 0
    cur = head
    while cur:
        count +=1
        cur = cur.next
    return count


racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(count_racers(racers1)) #4
print(count_racers(racers2)) #1
print(count_racers(None)) #0


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

def last_place(head):
    if not head:
        return None
    cur = head
    while cur.next is not None:
        cur = cur.next
    return cur.player_name

racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(last_place(racers1)) # Daisy
print(last_place(racers2)) # Mario
print(last_place(None)) # None