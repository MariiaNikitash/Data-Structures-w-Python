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
print(final_supply_costs([8, 4, 6, 2, 3])) 
#print(final_supply_costs([1, 2, 3, 4, 5])) 
#print(final_supply_costs([10, 1, 1, 6])) 


[4, 2, 4, 2, 3]
[1, 2, 3, 4, 5]
[9, 0, 1, 6]