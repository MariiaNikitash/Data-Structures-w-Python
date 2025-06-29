#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 1: Arrange Guest Arrival Order

def arrange_guest_arrival_order(arrival_pattern):
   guest_status = 1
   guest_order = []
   stack = []
   for c in arrival_pattern:
      if c == 'I' and not stack:
         guest_order += str(guest_status)
      if c == 'D':
         stack.append(guest_status)
      if c == 'I' and stack:
         stack.append(guest_status)
         while stack:
            guest_order += str(stack.pop())
            print(stack)

      guest_status += 1

   stack.append(guest_status)
   while stack:
      guest_order += str(stack.pop())

   return ''.join(guest_order)
#print(arrange_guest_arrival_order("IIIDIDDD"))  
#print(arrange_guest_arrival_order("DDD"))  

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 2
#Leetcode Medium: deckRevealedIncreasing
# Reveal Cards In Increasing Order 
from collections import deque
def deckRevealedIncreasing(deck):
   deck.sort()
   res = [0] * len(deck)
   q = deque(range(len(deck)))

   for card in deck:
      inx = q.popleft()
      res[inx] = card

      if q:
         q.append(q.popleft())
   return res
print(deckRevealedIncreasing([17,13,11,2,3,5,7])) 
print(deckRevealedIncreasing([1,1000])) 

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 3 

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 4 

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 5

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 6

