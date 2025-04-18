# Recursion

def repeat_hello(n):
	if n > 0:
		print("Hello", n)
    
		repeat_hello(n - 1)
		
#repeat_hello(5)

# Problem: 2
#Time Complexity: O(n) because we make n recursive calls.
#Space Complexity: O(n) because each recursive call adds a layer to the call stack, using more memory.
def factorial(num):
    # Action to repeat
    print(f"Count {num}")
    # Base case
    if num == 0:
        return 1
    #Recursive case
    else:
       return num * factorial(num-1)

#print(factorial(5))

# Iteravely it would take up O(1) space since no extra DS is used
def fac(n):
    res = 1
    for i in range(1, n+1):
        res *=i
    return res
#print(fac(5))


# Problem 3: Recursive Sum
def sum_list(lst):
    if lst == []:
        return 0
    print(lst[0])
    print(lst[1:])
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))

# The recursive calls stack up the additions, and they
# don’t happen all at once. The function keeps calling itself until it
# reaches the base case ([]), then starts adding the results back together.

# Problem 4: Recursive Power of 2
def is_power_of_two(n):
	pass

