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
#print(final_supply_costs([8, 4, 6, 2, 3])) [4,2,4,2,3]
#print(final_supply_costs([1, 2, 3, 4, 5]))  [1, 2, 3, 4, 5]
#print(final_supply_costs([10, 1, 1, 6]))  [9, 0, 1, 6]

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
 
#print(first_symmetrical_landmark(["canyon","forest","rotor","mountain", "ama"])) rotor
#print(first_symmetrical_landmark(["plateau","valley","cliff"])) " "

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 3: Terrain Elevation Match
def terrain_elevation_match(terrain):
    low,high = 0, len(terrain)
    res = []
    for i in range(len(terrain)):
        if terrain[i] == 'I':
            res.append(low)
            low +=1
        else:
            res.append(high)
            high -=1
    # Only one number remains — low == high
    res.append(low)  # or res.append(high)

    #if terrain[-1] == 'I':
    #    res.append(low)
    #else:
    #    res.append(high)
    return res

#print(terrain_elevation_match("IDID")) #[0, 4, 1, 3, 2]
#print(terrain_elevation_match("III")) #[0, 1, 2, 3]
#print(terrain_elevation_match("DDI")) #[3, 2, 0, 1]

#----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*
# Problem 4:


def find_the_log_conc_val(logs):
    if not logs:
        return 0
    if len(logs) == 1:
        return logs[0]
    l,r = 0, len(logs)-1
    res = 0
    while l<=r:
        if l == r:
            res += logs[l]
        else:
            concat = (str(logs[l]) + str(logs[r]))
            res += int(concat)
        l+=1
        r-=1

    return res

print(find_the_log_conc_val([7, 52, 2, 4])) #596
print(find_the_log_conc_val([5, 14, 13, 8, 12])) #673



