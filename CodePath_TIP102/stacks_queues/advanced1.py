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
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  

#123549876
#4321
