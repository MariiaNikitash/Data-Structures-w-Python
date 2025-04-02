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


def remove_tail(head):
    if head is None:
        #print("List is empty. No tail to remove.")
        return None
    if head.next is None:
        #print("Only one node in the list. Removing the node.")
        return None

    current = head
    while current.next.next:  # Stop at the second-to-last node
        #print(f"Current Node: {current.value} -> Next Node: {current.next.value}")
        current = current.next
    #print(f"Removing tail node with value: {current.next.value}")
    current.next = None
    return head


head = Node(1, Node(2, Node(3, Node(4))))

#print("Original List:")
#print_list(head)  # Print the original list

head = remove_tail(head)  # Remove the tail node

#print("List after removing tail:")
#print_list(head)  # Print the modified list

# 4. Find Middle

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    if not head:
        return False
    fast = head
    slow = head

    while fast and fast.next: 
        slow = slow.next         
        fast = fast.next.next
    return slow.value

# works for even and odd since when (for even) fast.next is None we still increment slow an return it
# for even since we reach the last node and we cant increment fast by 2 we return slow without increment
head = Node(1, Node(2, Node(3, Node(4))))
#print(find_middle_element(head))
# Input List:
# 1 -> 2 -> 3
# Input: head = 1
# Expected Return Value: 2


# 5. Is Palindrome
# Task: Given the head of a singly linked list, return True if the values of 
# linked list are palindromic and False otherwise. Use the two-pointer technique in your solution.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
    if not head:
        return False
    fast = head
    slow = head

    while fast and fast.next: 
        slow = slow.next         
        fast = fast.next.next
 # Reverse the second half of the list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    
    # Compare the first half and the reversed second half
    left, right = head, prev
    while right:  # Only need to compare till the end of the second half
        if left.value != right.value:
            return False
        left = left.next
        right = right.next
    
    return True
# Input List:
# 1 -> 2 -> 1
# Input: head = 1

# True

# 6. Put in Reverse