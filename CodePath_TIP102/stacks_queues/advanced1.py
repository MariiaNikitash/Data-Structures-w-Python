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
#print(deckRevealedIncreasing([17,13,11,2,3,5,7])) 
#print(deckRevealedIncreasing([1,1000])) 

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 3 
# Arrange Event Attendees by Priority. The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.
def arrange_attendees_by_priority(attendees, priority):
   less = []
   equal = []
   greater = []
   for a in attendees:
      if a < priority:
         less.append(a)
      elif a > priority:
         greater.append(a)
      else:
         equal.append(a)
   return less + equal + greater


print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) # [9,5,3,10,10,12,14]
# Or i can do a Dutch National Flag algorithm, but the order will not be preserved, i would use 3 pointers to partition into 3 groups and swap elements 
# Sort Colors: Leetcode Medium
def dutch_national_flag(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 4 

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 5

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 6

