# Linked Lists part 2


class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
#write a method attack() that takes in a Pokemon object opponent and decreases
# opponent's hp by their self's damage amount.

#If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the
# opponent's hp to 0 and print out "<Opponent name> fainted>.
#otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>"		
	def attack(self, opponent):
		opponent.hp -= self.damage
		if opponent.hp <= 0:
			opponent.hp = 0
			print(f"{opponent.name} fainted")
		else:
			print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
	
#pikachu = Pokemon("Pikachu", 35, 20)
#bulbasaur = Pokemon("Bulbasaur", 45, 30) 

#opponent = bulbasaur
#pikachu.attack(opponent)



class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

#print(node_1.value, "->", node_1.next.value)
#print(node_2.value, "->", node_2.next)

#Jigglypuff -> Wigglytuff
#Wigglytuff -> None


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	new_node.next = head
	return new_node


# Using the Linked List from Problem 2
#print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

#print(node_1.value, "->", node_1.next.value)
# Jigglypuff -> Wigglytuff 
# Ditto -> Jigglypuff


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next		
def get_tail(head):
	if not head:
		return None
	cur = head
	while cur.next:
		cur = cur.next
	return cur.value
	
num3 = Node('num3')
num2 = Node('num2', num3)
num1 = Node('num1', num2)
# linked list: num1->num2->num3
head = num1
tail = get_tail(num1)
#print(tail)


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	cur = head
	while cur:
		if cur.value == original:
			cur.value = replacement
		cur = cur.next
num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
#print(ll_replace(head, 5, "banana"))
# updated linked list: "banana" -> 6 -> "banana"
# To print the updated linked list:
current = head
while current:
    #print(current.value, end=" -> " if current.next else "\n")
    current = current.next



#6
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
	# List to store the values of nodes
    values = []
    # Start from the head node
    current = head
    # Counter to track the number of nodes processed
    count = 0
    # Loop until 'current' is not None and 'count' is less than 'n'
    while current is not None and count < n:
        # Append current node's value to the list
        values.append(current.value)
        # Move to the next node
        current = current.next
        # Increment the counter
        count += 1
    # Return the list of collected values
    return values
# linked list: a -> b -> c
#head = a
#lst = listify_first_n(head,2)
#print(lst)

# linked list: j -> k -> l 
#head2 = j
#lst2 = listify_first_n(head2,5)
#print(lst2)
#[`a`, `b`]
#[`j`, `k`, `l`]


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_insert(head, val, i):
    # Handle the case where the list is initially empty or `i` is 0
    if not head or i == 0:
        return Node(val, head)

    # Traverse to find the insertion point
    current = head
    count = 1  # Start count at 1 since we've already handled `i == 0`
    while current:
        # Insert at index `i` by adjusting the `next` pointers
        if count == i:
            new_node = Node(val, current.next)
            current.next = new_node
            return head
        current = current.next
        count += 1

    # If `i` was beyond the end, append to the last
    if count < i:
        current.next = Node(val)

    return head

# linked list: 3 -> 8 -> 12 -> 9
ll_insert(head, 20, 2)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9
# #

#8 Linked Listify
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def list_to_linked_list(lst):
	if not lst:
		return None
	head = Node(lst[0])
	current = head
	for value in lst[1:]:
		current.next = Node(value)
		current = current.next
	return head


normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list) # Only prints the head element!
# Linked list : Betty -> Veronica -> Archie -> Jughead


# 9
class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev

poliwag = Node('Poliwag')
poliwhirl = Node('Poliwhirl')
poliwrath = Node('Poliwrath')

poliwag.next = poliwhirl
poliwhirl.next = poliwrath

poliwrath.prev = poliwhirl
poliwhirl.prev = poliwag
#print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)
#Poliwag <-> Poliwhirl <-> Poliwrath

#10
class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def print_reverse(tail):
	cur = tail
	while cur:
		if cur.prev:
			print(cur.value, end=" ")
		else:
			print(cur.value)
		cur = cur.prev

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
print_reverse(poliwrath)
#Poliwrath Poliwhirl Poliwag

#--------------------- Problem Set Version 2 -------------------------------------
#                            (Below)


#--------------------- Problem Set Version 3 -------------------------------------
#                            (Below)
