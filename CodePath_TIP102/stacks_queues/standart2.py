#Problem 1: Final Costs After a Supply Discount
def final_supply_costs(costs):
    stack = []
    res = costs[:] # copy of costs
    for i in range(len(costs)):
        while stack and costs[stack[-1]] >= costs[i]:
            j = stack.pop()
            res[j] -= costs[i]
        stack.append(i)
    return res
#print(final_supply_costs([8, 4, 6, 2, 3])) 
#print(final_supply_costs([1, 2, 3, 4, 5])) 
#print(final_supply_costs([10, 1, 1, 6])) 

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 2: Find First Symmetrical Landmark Name

def first_symmetrical_landmark(landmarks):
    res = ''
    def palindrome(word):
        l,r = 0, len(word)-1
        while l < r:
            if word[l] != word[r]:
                return False
            l+=1
            r-=1
        return True
    
    for mark in landmarks:
        if (palindrome(mark)):
            res += mark
            return res
    return ''
    
    



print(first_symmetrical_landmark(["canyon","forest","rotor","mountain", "ama"])) 
print(first_symmetrical_landmark(["plateau","valley","cliff"])) 

#rotor