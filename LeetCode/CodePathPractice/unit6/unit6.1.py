# Linked Lists

# Temporary Head Technique
# When we solve linked list problems, we often encounter edge cases
# that involve the head of a linked list. Common edge cases involving
# the head of a linked list include:

# Deleting the current head of a linked list
# Adding a new element to the front of a linked list
# Reducing a linked list containing only one node to an empty list
# Adding a new node to an empty list

# 1. Nested Constructors
# Task: create the linked list 4 -> 3 -> 2 in a single assignment statement.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
head = Node(4, Node(3, Node(2)))

# 2. Find Frequency
# Task: Given the head of a linked list and a value val, return the frequency of val
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
	count = 0
	cur = head
	while cur:
		if cur.value == val:
			count+=1
			cur = cur.next
	return count


# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
# Output: 2

# 3. Remove Tail
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

#