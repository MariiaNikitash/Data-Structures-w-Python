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
	pass


# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1


# Output: 2